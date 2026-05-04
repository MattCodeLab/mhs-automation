"""
DuckDB loader for BNM MHS pipeline.

Each parsed DataFrame is written to `mhs.duckdb` as a table named
`{id_underscored}_{slug}`, e.g. `1_3_1_broad_money_m3`.

A companion `_catalog` table is maintained with one row per loaded table,
storing id, domain, title, row_count, date_range, frequencies, and column names.
"""

from __future__ import annotations

import json
from pathlib import Path

import duckdb
import pandas as pd

from pipeline.catalog import get_meta, table_name as catalog_table_name

DB_PATH = Path(__file__).resolve().parents[1] / "mhs.duckdb"

# ── public API ────────────────────────────────────────────────────────────────

def get_connection(db_path: Path = DB_PATH) -> duckdb.DuckDBPyConnection:
    return duckdb.connect(str(db_path))


def load_table(df: pd.DataFrame, table_id: str, con: duckdb.DuckDBPyConnection | None = None) -> dict:
    """Write df to DuckDB, replacing any existing table.

    Returns a summary dict:
      { table_name, table_id, domain, title, row_count, date_min, date_max, frequencies, columns }
    """
    meta       = get_meta(table_id)
    tname      = meta["table_name"]
    own_con    = con is None
    if own_con:
        con = get_connection()

    try:
        # Ensure date is datetime type
        if "date" in df.columns:
            df = df.copy()
            df["date"] = pd.to_datetime(df["date"])

        # DROP + CREATE (full reload)
        con.execute(f'DROP TABLE IF EXISTS "{tname}"')
        con.register("_tmp_df", df)
        con.execute(f'CREATE TABLE "{tname}" AS SELECT * FROM _tmp_df')
        con.unregister("_tmp_df")

        # Build summary
        row_count   = len(df)
        date_min    = df["date"].min().isoformat()[:10] if "date" in df.columns and not df["date"].isna().all() else None
        date_max    = df["date"].max().isoformat()[:10] if "date" in df.columns and not df["date"].isna().all() else None
        frequencies = sorted(df["frequency"].dropna().unique().tolist()) if "frequency" in df.columns else []
        columns     = [c for c in df.columns if c not in ("date", "frequency")]

        summary = {
            "table_name":  tname,
            "table_id":    table_id,
            "domain":      meta["domain"],
            "title":       meta["title"],
            "row_count":   row_count,
            "date_min":    date_min,
            "date_max":    date_max,
            "frequencies": json.dumps(frequencies),
            "columns":     json.dumps(columns),
        }

        _upsert_catalog(summary, con)
        return summary

    finally:
        if own_con:
            con.close()


def load_error(table_id: str, error: str, con: duckdb.DuckDBPyConnection | None = None) -> None:
    """Record a parse/load error in the catalog without writing a data table."""
    meta    = get_meta(table_id)
    own_con = con is None
    if own_con:
        con = get_connection()
    try:
        summary = {
            "table_name":  meta["table_name"],
            "table_id":    table_id,
            "domain":      meta["domain"],
            "title":       meta["title"],
            "row_count":   0,
            "date_min":    None,
            "date_max":    None,
            "frequencies": json.dumps([]),
            "columns":     json.dumps([]),
            "error":       error,
        }
        _upsert_catalog(summary, con)
    finally:
        if own_con:
            con.close()


def init_catalog(con: duckdb.DuckDBPyConnection) -> None:
    """Create the _catalog table if it doesn't exist."""
    con.execute("""
        CREATE TABLE IF NOT EXISTS _catalog (
            table_name  VARCHAR PRIMARY KEY,
            table_id    VARCHAR,
            domain      VARCHAR,
            title       VARCHAR,
            row_count   BIGINT,
            date_min    VARCHAR,
            date_max    VARCHAR,
            frequencies VARCHAR,   -- JSON array
            columns     VARCHAR,   -- JSON array
            error       VARCHAR    -- null if load succeeded
        )
    """)


# ── internals ─────────────────────────────────────────────────────────────────

def _upsert_catalog(summary: dict, con: duckdb.DuckDBPyConnection) -> None:
    init_catalog(con)
    con.execute("""
        INSERT OR REPLACE INTO _catalog
            (table_name, table_id, domain, title, row_count,
             date_min, date_max, frequencies, columns, error)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        summary.get("table_name"),
        summary.get("table_id"),
        summary.get("domain"),
        summary.get("title"),
        summary.get("row_count"),
        summary.get("date_min"),
        summary.get("date_max"),
        summary.get("frequencies"),
        summary.get("columns"),
        summary.get("error"),
    ])
