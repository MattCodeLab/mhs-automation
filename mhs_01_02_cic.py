import pandas as pd
import json
import numpy as np
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta as rd

from constants import MASTER_BUCKET
from helper import write_csv_parquet, derive_df_with_growth, get_recession_dates, get_cols_mhs

recession = get_recession_dates()
TEMPLATE_DASHBOARD = "dep/template_dashboard/cic.json"
OUTPUT_DASHBOARD = TEMPLATE_DASHBOARD.replace("dep/template_dashboard/", f"{MASTER_BUCKET}/dhdf/")

SRC_CIC_TS = "https://storage.data.gov.my/dashboards/currency_timeseries.parquet"
SRC_CIC_BM = "https://storage.data.gov.my/dashboards/currency_barmeter.parquet"

with open(TEMPLATE_DASHBOARD, "r") as f:
    data = json.load(f)


def format_num(x=None, perc=0, dp=1):
    if perc == 1:
        return f"{x:.1f}%"
    else:
        if x > 1e9:
            return f"{x/1e9:.{dp}f} billion"
        elif x > 1e6:
            return f"{x/1e6:.{dp}f} million"
        elif x > 1e3:
            return f"{x/1e3:.{dp}f} thousand"
        else:
            return f"{x:.{dp}f}"


def make_dashboard():

    # ----- Barmeter -----

    repl = {
        "note_proportion": "notes_pct",
        "note_number": "notes_volume",
        "coin_proportion": "coins_pct",
        "coin_number": "coins_volume",
        "note_1": "001_RM1",
        "note_5": "002_RM5",
        "note_10": "003_RM10",
        "note_20": "004_RM20",
        "note_50": "005_RM50",
        "note_100": "006_RM100",
        "coin_1": "001_1 sen",
        "coin_5": "002_5 sen",
        "coin_10": "003_10 sen",
        "coin_20": "004_20 sen",
        "coin_50": "005_50 sen",
        "others": "006_others",
    }

    df = pd.read_parquet(SRC_CIC_BM)
    for i in repl:
        df = df.replace(i, repl[i])
    df = df.sort_values(by=["chart", "variable"]).reset_index(drop=True)
    df = df.rename(columns={"chart": "chart_type"})
    df.variable = df.variable.str.split("_", expand=True)[1]
    df = df.rename(columns={"variable": "x", "value": "y"})
    df["t"] = df.y.apply(format_num)
    df.loc[df.chart_type.str.contains("_pct"), "t"] = df.y.apply(format_num, perc=1)

    for t in df.chart_type.unique():
        tf = df[df.chart_type == t].drop("chart_type", axis=1)
        if "volume" in t:
            tf["y"] = tf["y"].astype(int)
        else:
            tf["y"] = tf["y"].round(1)
        tf = tf.replace(np.nan, None)
        data["barmeter"]["data"][t]["values"] = tf.to_dict(orient="records")

    # ----- Timeseries -----

    df = pd.read_parquet(SRC_CIC_TS).replace("value", "value_rm").rename(columns={"date": "x"})
    df.x = pd.to_datetime(df.x)

    data_as_of = df.x.max()
    last_updated = data_as_of + rd(months=2) - rd(days=1)
    next_update = last_updated + rd(days=1) + rd(months=1) - rd(days=1)

    for k in ["metadata", "timeseries", "barmeter"]:
        data[k]["data_as_of"] = f"{data_as_of:%Y-%m-%d %H:%M:%S}"
    data["metadata"]["last_updated_at"] = f"Last update: {last_updated:%Y-%m-%d} 18:00"
    data["metadata"]["next_update_at"] = f"Next update: {next_update:%Y-%m-%d} 18:00"
    print(f"Data as of: {data_as_of:%Y-%m}")
    df.x = df.x.astype("int64") // 10**6

    for t in df.chart_type.unique():
        tf = df[df.chart_type == t].drop("chart_type", axis=1)
        if "growth" in t:
            for c in tf.columns[1:]:
                tf[c] = tf[c].round(1)
        tf = tf.replace(np.nan, None)
        for c in tf.columns:
            data["timeseries"]["data"][t][c] = tf[c].tolist()

    # ----- Write JSON out -----

    with open(OUTPUT_DASHBOARD, "w") as f:
        json.dump(data, f, ensure_ascii=True)
    print(f"Dashboard saved to {OUTPUT_DASHBOARD}")


if __name__ == "__main__":
    print("\n\n --------- Generating CIC dashboard  ----------\n")
    make_dashboard()

    print("\n\n --------- ✨✨✨ DONE ✨✨✨ ----------\n")
