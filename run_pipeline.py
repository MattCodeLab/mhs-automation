#!/usr/bin/env python3
"""
BNM MHS pipeline entry point.

Usage:
    python run_pipeline.py [--excel-dir sample-excels] [--db mhs.duckdb]

Scans the Excel directory, parses every .xlsx / .xls file, and loads
all tables into DuckDB.  Drop-in a new set of Excel files and re-run
to refresh everything.
"""

import argparse
import sys
import time
from pathlib import Path

import duckdb

# Ensure repo root is on path when run as a script
sys.path.insert(0, str(Path(__file__).parent))

from pipeline.catalog import get_meta, table_name as catalog_table_name
from pipeline.loader  import get_connection, init_catalog, load_table, load_error
from pipeline.parser  import parse_bnm_excel


def discover_files(excel_dir: Path) -> list[tuple[str, Path]]:
    """Return [(table_id, filepath), ...] sorted by table_id."""
    results = []
    for fp in sorted(excel_dir.glob("*.xls*")):
        stem = fp.stem           # e.g. "1.3.1"  "1.7a"  "4.8.c"
        results.append((stem, fp))
    return results


def run(excel_dir: Path, db_path: Path) -> None:
    files = discover_files(excel_dir)
    if not files:
        print(f"No Excel files found in {excel_dir}")
        return

    print(f"Found {len(files)} Excel files in {excel_dir}")
    print(f"Target database: {db_path}")
    print()

    con = get_connection(db_path)
    init_catalog(con)

    ok_count    = 0
    error_count = 0
    t0          = time.time()

    for i, (table_id, fp) in enumerate(files, 1):
        prefix = f"[{i:>3}/{len(files)}] {table_id:<18}"

        df, err = parse_bnm_excel(str(fp), table_id)

        if err:
            load_error(table_id, err, con)
            print(f"{prefix}  SKIP  {err}")
            error_count += 1
            continue

        try:
            summary = load_table(df, table_id, con)
            freqs   = ", ".join(summary["frequencies"].strip("[]").replace('"', '').split(", ")) if summary["frequencies"] != "[]" else "?"
            print(
                f"{prefix}  OK    {summary['row_count']:>6} rows  "
                f"{summary['date_min'] or '?'}..{summary['date_max'] or '?'}  "
                f"freq=[{freqs}]"
            )
            ok_count += 1
        except Exception as exc:
            load_error(table_id, str(exc), con)
            print(f"{prefix}  ERR   {exc}")
            error_count += 1

    con.close()

    elapsed = time.time() - t0
    print()
    print(f"Done in {elapsed:.1f}s — {ok_count} tables loaded, {error_count} skipped/errors")
    print(f"Database: {db_path.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="BNM MHS → DuckDB pipeline")
    parser.add_argument("--excel-dir", default="sample-excels", help="Directory with Excel files")
    parser.add_argument("--db",        default="mhs.duckdb",    help="DuckDB file path")
    args = parser.parse_args()

    excel_dir = Path(args.excel_dir)
    db_path   = Path(args.db)

    if not excel_dir.is_dir():
        print(f"Error: directory not found: {excel_dir}")
        sys.exit(1)

    run(excel_dir, db_path)


if __name__ == "__main__":
    main()
