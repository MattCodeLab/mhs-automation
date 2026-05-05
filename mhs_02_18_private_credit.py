import pandas as pd
import json
import numpy as np
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta as rd

from constants import MASTER_BUCKET
from helper import write_parquet, derive_df_with_growth, get_recession_dates, get_cols_mhs

recession = get_recession_dates()
TEMPLATE_DASHBOARD = "dep/template_dashboard/private_credit.json"
OUTPUT_DASHBOARD = TEMPLATE_DASHBOARD.replace("dep/template_dashboard/", f"{MASTER_BUCKET}/dhdf/")

with open(TEMPLATE_DASHBOARD, "r") as f:
    data = json.load(f)


def make_dashboard():

    col_initial = get_cols_mhs(db="private_credit", status="initial")
    col_final = get_cols_mhs(db="private_credit", status="final")

    pd.set_option("future.no_silent_downcasting", True)

    df = pd.read_excel("src/mhs/2.18.xlsx").iloc[15:, :7]
    df.columns = col_initial
    df["month"] = df["month"].astype(int).astype(str).str.zfill(2)
    df["year"] = df["year"].ffill().astype(str)
    df["date"] = pd.to_datetime(df["year"] + "-" + df["month"] + "-01")
    df = df[col_final]
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c] * 1e6).round(2)
    df = derive_df_with_growth(df=df, mom=1, col_exclude=["date"]).replace("abs", "value_rm")

    data["metadata"]["data_as_of"] = f"{df.date.max()}"
    data["timeseries"]["data_as_of"] = f"{df.date.max()}"
    data["metadata"][
        "last_updated_at"
    ] = f"Last update: {df.date.max()+rd(months=2)-rd(days=1):%Y-%m-%d} 19:00"
    data["metadata"][
        "next_update_at"
    ] = f"Next update: {df.date.max()+rd(months=3)-rd(days=1):%Y-%m-%d} 19:00"
    print(f"Data as of: {df.date.max():%Y-%m}")

    df["recession"] = df.date.isin(recession).astype(int)
    df.date = df.date.astype("int64") // 10**6
    df = df.rename(columns={"series": "chart_type", "date": "x"})

    for t in df.chart_type.unique():
        tf = df[df.chart_type == t].drop("chart_type", axis=1)
        for c in tf.columns:
            if c not in ["x", "recession"]:
                round_to = 2 if t == "value_rm" else 1
                tf[c] = tf[c].round(round_to)
        tf = tf.replace(np.nan, None)
        for c in tf.columns:
            data["timeseries"]["data"][t][c] = tf[c].tolist()

    with open(OUTPUT_DASHBOARD, "w") as f:
        json.dump(data, f, ensure_ascii=True)
    print(f"Dashboard saved to {OUTPUT_DASHBOARD}")


if __name__ == "__main__":
    print("\n\n --------- Generating Private Credit dashboard  ----------\n")
    make_dashboard()

    print("\n\n --------- ✨✨✨ DONE ✨✨✨ ----------\n")
