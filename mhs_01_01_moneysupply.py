import pandas as pd
import json
import numpy as np
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta as rd

from constants import MASTER_BUCKET
from helper import write_csv_parquet, derive_df_with_growth, get_recession_dates, get_cols_mhs

recession = get_recession_dates()
TEMPLATE_DASHBOARD = "dep/template_dashboard/money_supply.json"
OUTPUT_DASHBOARD = TEMPLATE_DASHBOARD.replace("dep/template_dashboard/", f"{MASTER_BUCKET}/dhdf/")

with open(TEMPLATE_DASHBOARD, "r") as f:
    data = json.load(f)


def make_dashboard():

    col_initial = get_cols_mhs(db="money_supply", status="initial")
    col_final = get_cols_mhs(db="money_supply", status="final")

    df = pd.read_excel("src/mhs/1.3.xlsx")
    df = df.replace("n.a.", np.nan)
    df.columns = ["check1", "check2"] + list(df.columns[2:])
    for c in ["check1", "check2"]:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)
    df = df.iloc[
        df[(df.check1 == 2013) & (df.check2 == 1)].index[0] :, 3 : 3 + 13
    ]  # if crash at this line --> add empty A column
    for c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(how="all").fillna(0)
    df.columns = col_initial
    df = df.multiply(1e6)
    df["date"] = [date(2013, 1, 1) + rd(months=x) for x in range(len(df))]
    df = df[col_final]

    cf = pd.melt(df.copy(), id_vars="date", value_vars=df.columns[1:], var_name="item")
    cf["measure"] = cf.item.str.split("_").str[0]
    cf["value"] /= 1e6
    cf = cf[["date", "measure", "item", "value"]]
    write_csv_parquet(f"{MASTER_BUCKET}/dhdc/money_supply", cf)

    df.date = pd.to_datetime(df.date)
    df = derive_df_with_growth(df, col_exclude=["date"], round_growth=1, mom=1, qoq=0, yoy=1)
    df["recession"] = df.date.isin(recession).astype(int)
    df = df.replace([np.inf, -np.inf], np.nan)
    df["series"] = df["series"].str.replace("abs", "value_rm")
    df = df.rename(columns={"date": "x"})

    data_as_of = df.x.max()
    last_updated = data_as_of + rd(months=2) - rd(days=1)
    next_update = last_updated + rd(days=1) + rd(months=1) - rd(days=1)

    data["timeseries"]["data_as_of"] = f"{data_as_of:%Y-%m-%d %H:%M:%S}"
    data["metadata"]["data_as_of"] = f"{data_as_of:%Y-%m-%d %H:%M:%S}"
    data["metadata"]["last_updated_at"] = f"Last update: {last_updated:%Y-%m-%d} 18:00"
    data["metadata"]["next_update_at"] = f"Next update: {next_update:%Y-%m-%d} 18:00"
    print(f"Data as of: {data_as_of:%Y-%m}")
    df.x = df.x.astype("int64") // 10**6

    for s in df.series.unique():
        tf = df[df.series == s].drop("series", axis=1)
        if "growth" in s:
            for c in tf.columns[1:]:
                tf[c] = tf[c].round(1)

        for c in tf.columns:
            data["timeseries"]["data"][s][c] = (
                tf[c].replace(np.nan, None).tolist()
            )  # None needed for JSON serializability

    with open(OUTPUT_DASHBOARD, "w") as f:
        json.dump(data, f, ensure_ascii=True)
    print(f"Dashboard saved to {OUTPUT_DASHBOARD}")


if __name__ == "__main__":
    print("\n\n --------- Generating Money Supply dashboard  ----------\n")
    make_dashboard()

    print("\n\n --------- ✨✨✨ DONE ✨✨✨ ----------\n")
