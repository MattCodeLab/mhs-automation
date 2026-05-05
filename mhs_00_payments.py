import pandas as pd
import json
import numpy as np
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta as rd

from constants import MASTER_BUCKET
from helper import write_csv_parquet, derive_df_with_growth, get_recession_dates, get_cols_mhs

recession = get_recession_dates()
TEMPLATE_DASHBOARD = "dep/template_dashboard/payment_xxx.json"
OUTPUT_DASHBOARD = TEMPLATE_DASHBOARD.replace("dep/template_dashboard/", f"{MASTER_BUCKET}/dhdf/")

cols = {
    "instruments": get_cols_mhs(db="payment_instruments", status="initial"),
    "systems": get_cols_mhs(db="payment_systems", status="initial"),
    "channels": get_cols_mhs(db="payment_channels", status="initial"),
}


def make_dashboard(db="instruments"):
    with open(TEMPLATE_DASHBOARD.replace("xxx", db), "r") as f:
        data = json.load(f)

    df = pd.read_excel(f"src/mhs/payment_{db}.xlsx").iloc[12:, 1:].dropna(how="all")
    df.columns = cols[db]
    for c in cols[db][1:]:
        df[c] = pd.to_numeric(df[c], errors="coerce") * 1e6
    df.date = pd.to_datetime(df.date)
    if db in ["systems"]:
        for c in cols[db][1:]:
            if "value_" in c:
                df[c] *= 1e3
    if db in ["instruments"]:
        for i in ["credit", "debit", "charge"]:
            for v in ["volume", "value"]:
                df[f"{v}_{i}_f2f"] -= df[f"{v}_{i}_online"]
    df = pd.melt(
        df, id_vars="date", value_vars=df.columns[1:], var_name="chart", value_name="value"
    )
    df[["variable", "chart"]] = df.chart.str.split(pat="_", n=1, expand=True)
    df = df.pivot(index=["variable", "date"], columns="chart", values="value").reset_index()

    data["metadata"]["data_as_of"] = f"{df.date.max()}"
    data["timeseries"]["data_as_of"] = f"{df.date.max()}"
    data["metadata"][
        "last_updated_at"
    ] = f"Last update: {df.date.max()+rd(months=2)+rd(days=9):%Y-%m-%d}"
    data["metadata"][
        "next_update_at"
    ] = f"Next update: {df.date.max()+rd(months=3)+rd(days=9):%Y-%m-%d}"

    df["recession"] = df.date.isin(recession).astype(int)
    df.date = df.date.astype("int64") // 10**6
    df = df.rename(columns={"variable": "chart_type", "date": "x"})

    for t in df.chart_type.unique():
        tf = df[df.chart_type == t].drop("chart_type", axis=1)
        for c in tf.columns:
            if c not in ["x", "recession"]:
                tf[c] = tf[c].round(1)
        tf = tf.replace(np.nan, None)
        for c in tf.columns:
            data["timeseries"]["data"][t][c] = tf[c].tolist()

    with open(OUTPUT_DASHBOARD.replace("xxx", db), "w") as f:
        json.dump(data, f, ensure_ascii=True)
        print(f"Dashboard saved to {OUTPUT_DASHBOARD.replace('xxx', db)}")


if __name__ == "__main__":
    print("\n\n --------- Generating Payments dashboards  ----------\n")
    for db in ["instruments", "systems", "channels"]:
        make_dashboard(db)

    print("\n\n --------- ✨✨✨ DONE ✨✨✨ ----------\n")
