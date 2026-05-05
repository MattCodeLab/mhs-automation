#!/usr/bin/env python3
"""
BNM MHS pipeline entry point.

Usage:
    python run_pipeline.py [--excel-dir sample-excels] [--db mhs.duckdb] [--export]

Scans the Excel directory, parses every .xlsx / .xls file, and loads
all tables into DuckDB.  Drop-in a new set of Excel files and re-run
to refresh everything.

--export   Also write CSV, Parquet, and JSON to the exports/ directory.
"""

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

import duckdb
import pandas as pd

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


def run(excel_dir: Path, db_path: Path, do_export: bool = False) -> None:
    files = discover_files(excel_dir)
    if not files:
        print(f"No Excel files found in {excel_dir}")
        return

    print(f"Found {len(files)} Excel files in {excel_dir}")
    print(f"Target database: {db_path}")
    if do_export:
        print(f"Export: CSV + Parquet + JSON → exports/")
    print()

    con = get_connection(db_path)
    init_catalog(con)

    ok_count    = 0
    error_count = 0
    t0          = time.time()

    # Collect per-table results for the report
    report_rows: list[dict] = []

    if do_export:
        from pipeline.exporter import export_table

    for i, (table_id, fp) in enumerate(files, 1):
        prefix = f"[{i:>3}/{len(files)}] {table_id:<18}"

        df, err = parse_bnm_excel(str(fp), table_id)

        if err:
            load_error(table_id, err, con)
            print(f"{prefix}  SKIP  {err}")
            error_count += 1
            report_rows.append({"table_id": table_id, "error": err})
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

            # Track column types for the report
            data_cols = json.loads(summary["columns"])
            numeric_cols = [
                c for c in df.columns
                if c not in ("date", "frequency")
                and pd.api.types.is_numeric_dtype(df[c])
            ]

            report_rows.append({
                "table_id":      table_id,
                "title":         summary["title"],
                "row_count":     summary["row_count"],
                "col_count":     len(data_cols),
                "numeric_count": len(numeric_cols),
                "date_min":      summary["date_min"],
                "date_max":      summary["date_max"],
                "frequencies":   freqs,
                "error":         None,
            })

            if do_export:
                export_table(df, table_id)

        except Exception as exc:
            load_error(table_id, str(exc), con)
            print(f"{prefix}  ERR   {exc}")
            error_count += 1
            report_rows.append({"table_id": table_id, "error": str(exc)})

    con.close()

    elapsed = time.time() - t0
    print()
    print(f"Done in {elapsed:.1f}s — {ok_count} tables loaded, {error_count} skipped/errors")
    print(f"Database: {db_path.resolve()}")

    _write_report(report_rows, excel_dir, db_path, elapsed)


def _write_report(
    report_rows: list[dict],
    excel_dir: Path,
    db_path: Path,
    elapsed: float,
) -> None:

    logs_dir = Path(__file__).parent / "logs"
    logs_dir.mkdir(exist_ok=True)

    date_str    = datetime.now().strftime("%Y%m%d")
    report_path = logs_dir / f"{date_str}_log.txt"

    ok_rows     = [r for r in report_rows if not r.get("error")]
    failed_rows = [r for r in report_rows if r.get("error")]

    total_cols    = sum(r.get("col_count", 0)     for r in ok_rows)
    total_numeric = sum(r.get("numeric_count", 0) for r in ok_rows)
    total_values  = sum(
        r.get("row_count", 0) * r.get("col_count", 0) for r in ok_rows
    )

    date_mins = [r["date_min"] for r in ok_rows if r.get("date_min")]
    date_maxs = [r["date_max"] for r in ok_rows if r.get("date_max")]
    span_min  = min(date_mins) if date_mins else "N/A"
    span_max  = max(date_maxs) if date_maxs else "N/A"

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = [
        "=" * 60,
        "BNM MHS Pipeline Run Report",
        "=" * 60,
        f"Run at    : {now}",
        f"Excel dir : {excel_dir.resolve()}",
        f"Database  : {db_path.resolve()}",
        f"Elapsed   : {elapsed:.1f}s",
        "",
        "── Summary ─────────────────────────────────────────────",
        f"Datasets processed : {len(report_rows)}",
        f"  Loaded OK        : {len(ok_rows)}",
        f"  Failed / skipped : {len(failed_rows)}",
        "",
        f"Total data columns : {total_cols}",
        f"Numeric columns    : {total_numeric}",
        f"Total data cells   : {total_values:,}",
        f"Date span          : {span_min}  →  {span_max}",
        "",
    ]

    if failed_rows:
        lines += [
            "── Failed / Skipped ─────────────────────────────────────",
            *[f"  {r['table_id']:<20} {r['error']}" for r in failed_rows],
            "",
        ]

    lines += [
        "── Loaded Tables ────────────────────────────────────────",
    ]
    for r in ok_rows:
        lines.append(
            f"  {r['table_id']:<12} {r['row_count']:>6} rows  "
            f"{r['col_count']:>3} cols  "
            f"{r['date_min'] or '?'}..{r['date_max'] or '?'}  "
            f"[{r['frequencies']}]"
        )

    lines += ["", "=" * 60]

    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"Report   : {report_path.resolve()}")


def main() -> None:

    parser = argparse.ArgumentParser(description="BNM MHS → DuckDB pipeline")
    parser.add_argument("--excel-dir", default="sample-excels", help="Directory with Excel files")
    parser.add_argument("--db",        default="mhs.duckdb",    help="DuckDB file path")
    parser.add_argument("--export",    action="store_true",     help="Export CSV / Parquet / JSON")
    args = parser.parse_args()

    excel_dir = Path(args.excel_dir)
    db_path   = Path(args.db)

    if not excel_dir.is_dir():
        print(f"Error: directory not found: {excel_dir}")
        sys.exit(1)

    run(excel_dir, db_path, do_export=args.export)


if __name__ == "__main__":
    import pandas as pd
    main()
