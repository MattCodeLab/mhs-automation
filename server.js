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
  // Return date + up to 8 numeric columns as a time series
  // Optionally filter by frequency
  const freqFilter = params.get("freq");

  // Discover numeric columns
  const colRows = await queryObj(`
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = '${tableName}'
      AND table_schema = 'main'
      AND column_name NOT IN ('date','frequency')
    ORDER BY ordinal_position
  `);

  const numericCols = colRows
    .filter(r => /INT|FLOAT|DOUBLE|DECIMAL|BIGINT|HUGEINT/i.test(r.data_type))
    .slice(0, 8)
    .map(r => r.column_name);

  if (!numericCols.length) return json({ cols: [], rows: [] });

  const colList = numericCols.map(c => `"${c}"`).join(", ");
  const where   = freqFilter ? `WHERE frequency = '${freqFilter}'` : "";

  const rows = await queryObj(
    `SELECT date::VARCHAR AS date, frequency, ${colList}
     FROM "${tableName}"
     ${where}
     ORDER BY date`
  );

  return json({ cols: numericCols, rows });
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
