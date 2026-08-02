"""
CHALLENGE PART 1 of 3: Load the Data

This project analyses one month of (pretend) daily stock-level readings
from the The Trendiest stockroom, stored in stock_levels.csv. It's split
into 3 files:
    data_loader.py  - (this file) loads the CSV into a usable table
    visualise.py    - turns that table into charts
    main.py         - runs everything and saves the charts as images

stock_levels.csv has these columns:
    date         - the date of the stock reading, e.g. "2026-07-01"
    item         - the stockroom item being tracked
    stock_level  - how many units of that item were on hand that day

YOUR TASK (this file)
----------------------
Use the pandas library to load the CSV file into a DataFrame (think of it
like a spreadsheet you can work with in code).
"""

import pandas as pd


def load_stock_levels(csv_path="stock_levels.csv"):
    """
    Read csv_path using pandas and return it as a DataFrame.

    Hint:
        return pd.read_csv(csv_path)
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    df = load_stock_levels()
    print(df.head())  # show the first 5 rows
    print("\nColumn names:", list(df.columns))
    print("Total rows:", len(df))
    print("Items tracked:", sorted(df["item"].unique()))
