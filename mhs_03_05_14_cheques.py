import pandas as pd
import json
import numpy as np
from dateutil.relativedelta import relativedelta as rd

from constants import MASTER_BUCKET
from helper import derive_df_with_growth, get_recession_dates

pd.set_option("future.no_silent_downcasting", True)

recession = get_recession_dates()
TEMPLATE_DASHBOARD = "dep/template_dashboard/cheques.json"
OUTPUT_DASHBOARD = TEMPLATE_DASHBOARD.replace("dep/template_dashboard/", f"{MASTER_BUCKET}/dhdf/")

with open(TEMPLATE_DASHBOARD, "r") as f:
    data = json.load(f)


def make_dashboard():

    col_numeric = {
        "cleared_volume": 1e6,
        "cleared_value": 1e9,
        "returned_volume": 1e3,
        "returned_value": 1e6,
        "returned_insufficient_volume": 1e3,
        "returned_insufficient_value": 1e6,
    }

    df = pd.read_excel("src/mhs/3.5.14.xlsx")
    df.columns = ["drop", "year", "month"] + list(col_numeric.keys())
    df = df.drop("drop", axis=1).dropna(subset=["month"])
    df.year = df.year.ffill()
    df = df.dropna(subset=["year"])
    df.year = df.year.astype(int).astype(str)
    df.month = df.month.astype(int).astype(str).str.zfill(2)
    df["date"] = pd.to_datetime(df.year + df.month, format="%Y%m")
    df = df[["date"] + list(col_numeric.keys())]
    for c in col_numeric:
        df[c] = pd.to_numeric(df[c], errors="coerce") * col_numeric[c]
    df["returned_other_volume"] = df["returned_volume"] - df["returned_insufficient_volume"]
    df["returned_other_value"] = df["returned_value"] - df["returned_insufficient_value"]
    df = df.drop(columns=["returned_volume", "returned_value"])

    df = pd.melt(df, id_vars=["date"], value_vars=df.columns[1:])
    df[["cheque_type", "variable"]] = df.variable.str.rsplit("_", n=1, expand=True)
    df = df.pivot_table(
        index=["date", "variable"], columns="cheque_type", values="value"
    ).reset_index()
    df = df.sort_values(by=["variable", "date"]).reset_index(drop=True)
    df = derive_df_with_growth(df, col_exclude=["date", "variable"], round_growth=1, mom=0, yoy=1)
    df = df.rename(columns={"date": "x", "series": "chart_type"})
    df["chart_type"] = df["chart_type"] + "_" + df["variable"]
    df = (
        df.drop(columns=["variable"])
        .replace("abs_value", "value_rm")
        .replace("abs_volume", "volume")
    )
    df["recession"] = df.x.isin(recession).astype(int)

    data_as_of = df.x.max()
    last_updated = data_as_of + rd(months=2) - rd(days=1)
    next_update = last_updated + rd(days=1) + rd(months=1) - rd(days=1)

    data["timeseries"]["data_as_of"] = f"{data_as_of:%Y-%m-%d %H:%M:%S}"
    data["metadata"]["data_as_of"] = f"{data_as_of:%Y-%m-%d %H:%M:%S}"
    data["metadata"]["last_updated_at"] = f"Last update: {last_updated:%Y-%m-%d} 18:00"
    data["metadata"]["next_update_at"] = f"Next update: {next_update:%Y-%m-%d} 18:00"
    print(f"Data as of: {data_as_of:%Y-%m}")
    df.x = df.x.astype("int64") // 10**3

    for t in df.chart_type.unique():
        tf = df[df.chart_type == t].drop("chart_type", axis=1)
        if "growth" in t:
            for c in tf.columns[1:]:
                round_to = 0 if "volume" in t else 2
                tf[c] = tf[c].round(round_to)
        tf = tf.replace(np.nan, None)
        for c in tf.columns:
            data["timeseries"]["data"][t][c] = tf[c].tolist()
    with open(OUTPUT_DASHBOARD, "w") as f:
        json.dump(data, f, ensure_ascii=True)
    print(f"Dashboard saved to {OUTPUT_DASHBOARD}")


if __name__ == "__main__":
    print("\n\n --------- Generating Cheques dashboard  ----------\n")
    make_dashboard()

    print("\n\n --------- ✨✨✨ DONE ✨✨✨ ----------\n")
