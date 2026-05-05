/**
 * BNM MHS data browser – Bun HTTP server
 *
 * Run:  bun run server.js
 * Open: http://localhost:3000
 *
 * API
 *   GET /api/tables              → catalog summary (all tables)
 *   GET /api/table/:name         → schema + stats for one table
 *   GET /api/table/:name/series  → time-series data (date + numeric cols)
 */

import { DuckDBInstance } from "@duckdb/node-api";
import { readFileSync } from "fs";
import { join } from "path";

const PORT    = 3000;
const DB_PATH = join(import.meta.dir, "mhs.duckdb");

// ── DuckDB setup ──────────────────────────────────────────────────────────────

const instance   = await DuckDBInstance.create(DB_PATH, { access_mode: "READ_ONLY" });
const connection = await instance.connect();

async function query(sql, params = []) {
  const reader = await connection.runAndReadAll(sql);
  return reader.getRows();                 // array of row-arrays
}

async function queryObj(sql) {
  const reader = await connection.runAndReadAll(sql);
  const cols   = reader.columnNames();
  return reader.getRows().map(row =>
    Object.fromEntries(cols.map((c, i) => [c, row[i]]))
  );
}

// ── routing ───────────────────────────────────────────────────────────────────

const HANDLERS = [
  [/^GET \/api\/tables$/,                 handleCatalog],
  [/^GET \/api\/table\/([^/]+)\/series$/, handleSeries],
  [/^GET \/api\/table\/([^/]+)$/,         handleTable],
  [/^GET \//,                             handleStatic],
];

Bun.serve({
  port: PORT,
  async fetch(req) {
    const url    = new URL(req.url);
    const key    = `${req.method} ${url.pathname}`;
    const params = url.searchParams;

    for (const [re, handler] of HANDLERS) {
      const m = key.match(re);
      if (m) {
        try {
          return await handler(req, m[1], params);
        } catch (e) {
          console.error(e);
          return json({ error: String(e) }, 500);
        }
      }
    }
    return new Response("Not found", { status: 404 });
  },
});

console.log(`BNM MHS browser → http://localhost:${PORT}`);

// ── handlers ──────────────────────────────────────────────────────────────────

async function handleCatalog() {
  const rows = await queryObj(`
    SELECT
      table_name,
      table_id,
      domain,
      title,
      row_count,
      date_min,
      date_max,
      frequencies,
      columns,
      error
    FROM _catalog
    ORDER BY table_id
  `);
  // Parse JSON fields
  rows.forEach(r => {
    r.frequencies = safeJson(r.frequencies, []);
    r.columns     = safeJson(r.columns, []);
  });
  return json(rows);
}

async function handleTable(_, tableName) {
  // Catalog entry
  const cat = await queryObj(
    `SELECT * FROM _catalog WHERE table_name = '${tableName}'`
  );
  if (!cat.length) return json({ error: "Table not found" }, 404);
  const meta = cat[0];
  meta.frequencies = safeJson(meta.frequencies, []);
  meta.columns     = safeJson(meta.columns, []);

  // Column stats (min/max/null_count per numeric col, distinct for strings)
  const sample = await queryObj(
    `SELECT date::VARCHAR AS date, * EXCLUDE (date) FROM "${tableName}" LIMIT 5`
  );

  // Column-level stats
  const colStats = [];
  for (const col of meta.columns) {
    const qcol = `"${col}"`;
    try {
      const stats = await queryObj(
        `SELECT
           MIN(${qcol})::VARCHAR  AS min_val,
           MAX(${qcol})::VARCHAR  AS max_val,
           COUNT(${qcol})         AS non_null,
           COUNT(*) - COUNT(${qcol}) AS null_count
         FROM "${tableName}"`
      );
      colStats.push({ column: col, ...stats[0] });
    } catch {
      colStats.push({ column: col });
    }
  }

  return json({ meta, sample, col_stats: colStats });
}

async function handleSeries(_, tableName, params) {
  const freqFilter = params.get("freq");

  // Classify all columns
  const colInfo = await queryObj(`
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = '${tableName}' AND table_schema = 'main'
    ORDER BY ordinal_position
  `);

  const META = new Set(["date", "frequency"]);
  const isNumeric = r => /INT|FLOAT|DOUBLE|DECIMAL|BIGINT|HUGEINT/i.test(r.data_type);
  const dimCols = colInfo.filter(r => !META.has(r.column_name) && !isNumeric(r)).map(r => r.column_name);
  const numCols = colInfo.filter(r => !META.has(r.column_name) &&  isNumeric(r)).map(r => r.column_name);

  // ── Indicator / long-format tables (from wide parser) ──────────────────────
  // These have an "indicator" string col + a single "value" numeric col.
  // Pivot so each indicator becomes its own column.
  if (dimCols.includes("indicator") && numCols.includes("value")) {
    const freqCond = freqFilter ? `AND frequency = ${sqlLit(freqFilter)}` : "";
    const indRows  = await queryObj(`
      SELECT indicator, COUNT(*) AS cnt
      FROM "${tableName}"
      WHERE indicator IS NOT NULL ${freqCond}
      GROUP BY indicator ORDER BY cnt DESC LIMIT 20
    `);
    const indicators = indRows.map(r => r.indicator);
    if (!indicators.length) return json({ cols: [], rows: [], col_types: {}, col_labels: {} });

    const caseExprs = indicators.map((ind, i) =>
      `MAX(CASE WHEN indicator = '${ind.replace(/'/g, "''")}' THEN value END) AS "ind_${i}"`
    ).join(", ");
    const where = freqFilter ? `WHERE frequency = ${sqlLit(freqFilter)}` : "";
    const rows  = await queryObj(`
      SELECT date::VARCHAR AS date, frequency, ${caseExprs}
      FROM "${tableName}" ${where}
      GROUP BY date, frequency ORDER BY date
    `);

    const cols      = indicators.map((_, i) => `ind_${i}`);
    const colLabels = Object.fromEntries(indicators.map((ind, i) => [`ind_${i}`, ind]));
    const colTypes  = Object.fromEntries(indicators.map((ind, i) => [`ind_${i}`, inferDataType(ind)]));
    return json({ cols, rows, col_types: colTypes, col_labels: colLabels });
  }

  // ── Standard wide-format tables ────────────────────────────────────────────
  const conds = [];
  if (freqFilter) conds.push(`frequency = ${sqlLit(freqFilter)}`);

  // When a dimension column exists (sector, type, purpose…), filter to the
  // aggregate "Total" row so one row per date reaches the chart.
  if (dimCols.length > 0) {
    const dimCol   = dimCols[0];
    const totCheck = await queryObj(`
      SELECT COUNT(*) AS cnt FROM "${tableName}"
      WHERE LOWER("${dimCol}") LIKE '%total%' OR LOWER("${dimCol}") LIKE '%jumlah%'
    `);
    if (Number(totCheck[0].cnt) > 0) {
      conds.push(`(LOWER("${dimCol}") LIKE '%total%' OR LOWER("${dimCol}") LIKE '%jumlah%')`);
    }
  }

  const where     = conds.length ? `WHERE ${conds.join(" AND ")}` : "";
  const selCols   = numCols.slice(0, 20);
  if (!selCols.length) return json({ cols: [], rows: [], col_types: {}, col_labels: {} });

  // MAX() aggregation de-duplicates any remaining rows for the same date.
  const colList = selCols.map(c => `MAX("${c}") AS "${c}"`).join(", ");
  const rows    = await queryObj(`
    SELECT date::VARCHAR AS date, frequency, ${colList}
    FROM "${tableName}" ${where}
    GROUP BY date, frequency ORDER BY date
  `);

  const colTypes = Object.fromEntries(numCols.map(c => [c, inferDataType(c)]));
  return json({ cols: selCols, rows, col_types: colTypes, col_labels: {} });
}

// ── data-type inference ───────────────────────────────────────────────────────

function inferDataType(col) {
  // Normalise: lower-case, collapse non-alphanumeric to underscores
  const n = col.toLowerCase().replace(/[^a-z0-9]+/g, "_");

  // Volume / count
  if (/^no_of|_no_of|^no_million|^no_000|number_of|_count$|^count_|^volume|_volume$|^num_of|transactions?$|principal_card|supplementary_card|polic|certif|cases_|cleared|returned/.test(n))
    return "volume";

  // Percentage / rate
  if (/^ratio_|_ratio$|_ratio_|growth$|_growth$|_rate$|^rate_|yield|coverage|spread|adequacy|retention|_percent|_pct$|capital_adequacy|claims_ratio|bps|weighted/.test(n))
    return "pct";

  // RM / monetary
  if (/outstanding|approved|disbursed|repaid|asset|liabilit|deposit|loan|financing|expenditure|reserve|debt|bond|sukuk|premium|claim|contribut|income|provision|impaired|npl|amount|balance|capital|raised|turnover|fund|^rm_|_rm_|_rm$/.test(n))
    return "rm";

  // Default: financial data is predominantly monetary
  return "rm";
}

function sqlLit(s) {
  return `'${String(s).replace(/'/g, "''")}'`;
}

function handleStatic(req) {
  const url      = new URL(req.url);
  let   filePath = url.pathname === "/" ? "/index.html" : url.pathname;
  filePath       = join(import.meta.dir, "public", filePath);

  try {
    const body = readFileSync(filePath);
    const ct   = filePath.endsWith(".html") ? "text/html"
               : filePath.endsWith(".js")   ? "application/javascript"
               : filePath.endsWith(".css")  ? "text/css"
               : "application/octet-stream";
    return new Response(body, { headers: { "Content-Type": ct } });
  } catch {
    return new Response("Not found", { status: 404 });
  }
}

// ── helpers ───────────────────────────────────────────────────────────────────

function json(data, status = 200) {
  return new Response(JSON.stringify(data, (_k, v) => typeof v === "bigint" ? Number(v) : v), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

function safeJson(s, fallback) {
  try { return JSON.parse(s); } catch { return fallback; }
}
