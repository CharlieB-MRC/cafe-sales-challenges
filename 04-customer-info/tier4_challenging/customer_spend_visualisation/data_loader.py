"""
CHALLENGE PART 1 of 3: Load the Data

This project analyses The Trendiest's loyalty card customer records, stored
in customer_spend.csv. It's split into 3 files:
    data_loader.py  - (this file) loads the CSV into a usable table
    visualise.py    - turns that table into charts
    main.py          - runs everything and saves the charts as images

customer_spend.csv has these columns:
    customer_name  - the loyalty card member's name
    total_spend    - how much they've spent at the café in total ($)
    visits         - how many times they've visited
    loyalty_tier   - their current tier: "Bronze", "Silver", or "Gold"

YOUR TASK (this file)
----------------------
Use the pandas library to load the CSV file into a DataFrame (think of it
like a spreadsheet you can work with in code).
"""

import pandas as pd


def load_customers(csv_path="customer_spend.csv"):
    """
    Read csv_path using pandas and return it as a DataFrame.

    Hint:
        return pd.read_csv(csv_path)
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    df = load_customers()
    print(df.head())  # show the first 5 rows
    print("\nColumn names:", list(df.columns))
    print("Total customers:", len(df))
