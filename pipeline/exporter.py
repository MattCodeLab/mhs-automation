"""
Export module for BNM MHS pipeline.

Writes each parsed DataFrame to:
  exports/<table_name>/<table_name>.csv
  exports/<table_name>/<table_name>.parquet
  exports/<table_name>/<table_name>.json  (last N observations + metadata block)

Per-dataset config lives in:
  exports/config/<table_name>.json

Config schema:
  {
    "json_last_n": 10,           -- how many recent observations to include in JSON
    "metadata": { ... }          -- arbitrary key/values merged into JSON metadata block
  }
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from pipeline.catalog import get_meta

EXPORTS_DIR = Path(__file__).resolve().parents[1] / "exports"
CONFIG_DIR  = EXPORTS_DIR / "config"


# ── public API ────────────────────────────────────────────────────────────────

def export_table(df: pd.DataFrame, table_id: str) -> dict[str, str]:
    """Export df for one table to CSV, Parquet, and JSON.

    Returns a dict of { format: absolute_path }.
    Writes a default config file if none exists yet.
    """
    meta   = get_meta(table_id)
    tname  = meta["table_name"]
    config = _load_or_init_config(tname, meta)

    out_dir = EXPORTS_DIR / tname
    out_dir.mkdir(parents=True, exist_ok=True)

    results: dict[str, str] = {}

    # ── CSV ───────────────────────────────────────────────────────────────────
    csv_path = out_dir / f"{tname}.csv"
    df.to_csv(csv_path, index=False)
    results["csv"] = str(csv_path)

    # ── Parquet ───────────────────────────────────────────────────────────────
    parquet_path = out_dir / f"{tname}.parquet"
    df.to_parquet(parquet_path, index=False)
    results["parquet"] = str(parquet_path)

    # ── JSON (last N observations + metadata) ─────────────────────────────────
    n      = config.get("json_last_n", 10)
    recent = df.tail(n)

    date_min = df["date"].min().isoformat()[:10] if "date" in df.columns and df["date"].notna().any() else None
    date_max = df["date"].max().isoformat()[:10] if "date" in df.columns and df["date"].notna().any() else None

    metadata_block: dict = {
        "table_id":      table_id,
        "title":         meta["title"],
        "domain":        meta["domain"],
        "exported_at":   datetime.now(timezone.utc).isoformat(),
        "total_rows":    len(df),
        "exported_rows": len(recent),
        "date_min":      date_min,
        "date_max":      date_max,
    }
    metadata_block.update(config.get("metadata", {}))

    payload = {
        "metadata": metadata_block,
        "records":  recent.to_dict(orient="records"),
    }

    json_path = out_dir / f"{tname}.json"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, default=_json_default, indent=2, ensure_ascii=False)
    results["json"] = str(json_path)

    return results


# ── config helpers ────────────────────────────────────────────────────────────

def _load_or_init_config(table_name: str, meta: dict) -> dict:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    config_path = CONFIG_DIR / f"{table_name}.json"

    if config_path.exists():
        with open(config_path, encoding="utf-8") as fh:
            return json.load(fh)

    default = {
        "json_last_n": 10,
        "metadata": {
            "source": "Bank Negara Malaysia Monthly Highlights Statistics",
            "url":    "https://www.bnm.gov.my/publications/mhs",
            "notes":  "",
        },
    }
    with open(config_path, "w", encoding="utf-8") as fh:
        json.dump(default, fh, indent=2)
    return default


def _json_default(obj):
    if isinstance(obj, pd.Timestamp):
        return obj.isoformat()[:10]
    if hasattr(obj, "isoformat"):
        return obj.isoformat()
    return str(obj)
