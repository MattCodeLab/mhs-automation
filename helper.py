"""
This module provides utility functions for data handling in data engineering workflows
"""

import pandas as pd
import re
import boto3
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import time


# upload file to bucket (S3)
# def upload_s3(bucket_name, source_file_name, cloud_file_name=None):
#     """
#     Upload a local file to an AWS S3 bucket.
#
#     Args:
#         bucket_name (str): The name of the S3 bucket.
#         source_file_name (str): The local path of the file to upload.
#         cloud_file_name (str, optional): The destination name on S3. If None, uses the source file's name.
#
#     Returns:
#         str: A message indicating success or the nature of the failure.
#     """
#     if not cloud_file_name:
#         cloud_file_name = source_file_name
#     try:
#         time_start_temp = time.time()
#         s3 = boto3.client(
#             "s3", aws_access_key_id=TOKEN_API_S3[0], aws_secret_access_key=TOKEN_API_S3[1]
#         )
#         s3.upload_file(f"{bucket_name}/{source_file_name}", bucket_name, cloud_file_name)
#         duration = "{:.1f}".format(time.time() - time_start_temp) + " seconds"
#         res = f"SUCCESS ({duration}): {bucket_name}/{cloud_file_name}"
#     except Exception as e:
#         res = f"FAILURE: {bucket_name}/{source_file_name}\n\n{e}"
#
#     return res


def write_csv_parquet(FILEPATH, df=None):
    """
    Export a pandas DataFrame to both CSV and Parquet (Brotli-compressed) formats.

    Args:
        FILEPATH (str): The file path without extension. E.g., "results/mydata".
        df (pd.DataFrame): The DataFrame to be written.

    The function writes both `FILEPATH.csv` and `FILEPATH.parquet`.
    """
    df.to_csv(f"{FILEPATH}.csv", index=False)
    df.to_parquet(f"{FILEPATH}.parquet", index=False, compression="brotli")
    print(f"Wrote CSV + Parquet: {FILEPATH}")


def write_parquet(FILEPATH, df=None):
    """
    Export a pandas DataFrame to a Brotli-compressed Parquet file.

    Args:
        FILEPATH (str): The file path without extension.
        df (pd.DataFrame): The DataFrame to be written.

    The function writes to `FILEPATH.parquet`.
    """
    df.to_parquet(f"{FILEPATH}.parquet", index=False, compression="brotli")
    print(f"Wrote Parquet: {FILEPATH}")


def write_csv(FILEPATH, df=None):
    """
    Export a pandas DataFrame to a CSV file.

    Args:
        FILEPATH (str): The file path without extension.
        df (pd.DataFrame): The DataFrame to be written.

    The function writes to `FILEPATH.csv`.
    """
    df.to_csv(f"{FILEPATH}.csv", index=False)
    print(f"Wrote CSV: {FILEPATH}")


def derive_df_with_growth(
    df=None,
    col_exclude=[],
    col_groupby=[],
    round_growth=1,
    mom=1,
    qoq=0,
    yoy=1,
    periods_mom=1,
    periods_qoq=4,
    periods_yoy=12,
    melt=0,
    melt_names=["variable", "value"],
):
    """
    Compute growth rates (yoy, mom, qoq) for all columns of a DataFrame, optionally melting the result.

    Args:
        df (pd.DataFrame): The input DataFrame on which to compute growth rates.
        col_exclude (list, optional): Columns to exclude from growth calculations (plus "series" always).
        col_groupby (list, optional): Columns to group by for growth calculations.
        round_growth (int, optional): Number of decimals to round growth results.
        mom (int, optional): If 1, compute month-on-month growth.
        qoq (int, optional): If 1, compute quarter-on-quarter growth. (Don't use together with mom!)
        yoy (int, optional): If 1, compute year-on-year growth.
        periods_mom (int, optional): Number of periods for mom growth (usually 1).
        periods_qoq (int, optional): Number of periods for qoq (usually 4 for quarterly data).
        periods_yoy (int, optional): Number of periods for yoy (usually 12 for monthly data).
        melt (int, optional): If 1, return DataFrame in melted "long" format.
        melt_names (list, optional): Names for the variable and value columns in melt.

    Returns:
        pd.DataFrame: DataFrame with absolute values and growth rates, optionally in melted format.

    Raises:
        AssertionError: If both mom and qoq are set to 1 (they are not generally compatible).

    Notes:
        - Always adds a "series" column identifying the type ("abs", "growth_yoy", "growth_mom", "growth_qoq").
        - Each growth type is added as a separate set of rows in the DataFrame.
    """
    assert mom + qoq < 2, "DANGER: Likely computing mom and qoq from same data!!"

    col_exclude = ["series"] + col_exclude
    col_include = [x for x in df.columns if x not in col_exclude]

    # Identify columns with negative values (not used further, but could be for e.g. log diff)
    col_negative = []
    for c in col_include:
        if len(df[df[c] < 0]) > 0:
            col_negative += [c]

    # Set initial series as absolute
    df = df.assign(series="abs")[["series"] + list(df.columns)]

    if len(col_groupby) == 0:
        col_groupby = ["series"]

    if yoy == 1:
        dfy = df.copy().assign(series="growth_yoy")
        for c in col_include:
            dfy[c] = (
                dfy.groupby(col_groupby)[c].pct_change(periods=periods_yoy, fill_method=None) * 100
            ).round(round_growth)
        dfy = dfy.dropna(subset=col_include, how="all")
    else:
        dfy = pd.DataFrame(columns=df.columns)

    if mom == 1:
        dfm = df.copy().assign(series="growth_mom")
        for c in col_include:
            dfm[c] = (
                dfm.groupby(col_groupby)[c].pct_change(periods=periods_mom, fill_method=None) * 100
            ).round(round_growth)
        dfm = dfm.dropna(subset=col_include, how="all")
    else:
        dfm = pd.DataFrame(columns=df.columns)

    if qoq == 1:
        dfq = df.copy().assign(series="growth_qoq")
        for c in col_include:
            dfq[c] = (
                dfq.groupby(col_groupby)[c].pct_change(periods=periods_qoq, fill_method=None) * 100
            ).round(round_growth)
        dfq = dfq.dropna(subset=col_include, how="all")
    else:
        dfq = pd.DataFrame(columns=df.columns)

    dfs_to_concat = [x for x in [df, dfy, dfm, dfq] if len(x) > 0]
    df = pd.concat(dfs_to_concat, axis=0, ignore_index=True)

    if melt == 1:
        df = pd.melt(
            df,
            id_vars=col_exclude,
            value_vars=col_include,
            var_name=melt_names[0],
            value_name=melt_names[1],
        ).sort_values(by=col_exclude)
        df = pd.concat(
            [
                df[df.series == "abs"],
                df[df.series == "growth_yoy"],
                df[df.series == "growth_mom"],
                df[df.series == "growth_qoq"],
            ],
            axis=0,
            ignore_index=True,
        )

    return df


def get_recession_dates():
    """
    Retrieves a list of recession dates based on a binary flag.

    Dependencies:
        'dep/flag_binary.csv' file, which should contain a 'date' column and a 'flag_recession_business' column.
        The function filters rows where 'flag_recession_business' is 1 (indicating recession periods),
        converts the 'date' column to datetime, and returns a list of corresponding dates.

    Returns:
        list: List of datetime.date objects representing the start dates of recessions.
    """
    rf = pd.read_csv("dep/flag_binary.csv")
    rf.date = pd.to_datetime(rf.date)
    all_dates = pd.date_range(start=rf.date.min(), end=rf.date.max(), freq="D")
    rf = rf.set_index("date").reindex(all_dates).reset_index().rename(columns={"index": "date"})
    for c in rf.columns[1:]:
        rf[c] = rf[c].ffill().astype(int)
    recession = rf[rf.flag_recession_business == 1]["date"].tolist()
    return recession


def get_cols_mhs(db=None, status=None):
    """
    Retrieves a list of columns for a given database and status.
    """
    cols = pd.read_csv("dep/cols_mhs.csv")
    cols = cols[cols.db == db]
    cols = cols[cols.status == status]
    return cols.col.tolist()


# next function
