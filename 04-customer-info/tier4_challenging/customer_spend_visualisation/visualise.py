"""
CHALLENGE PART 2 of 3: Chart the Data

Complete data_loader.py first. This file turns the customers DataFrame
into two charts using matplotlib.

YOUR TASK (this file)
----------------------
Implement both functions below. Each one should build a chart using
matplotlib and matplotlib's `savefig` should NOT be called here — that
happens in main.py. Just build the chart with plt (it will be shown or
saved by whoever calls these functions).
"""

import matplotlib.pyplot as plt


def plot_spend_distribution(df):
    """
    Create a histogram showing the distribution of total_spend across all
    customers (i.e. how many customers fall into each spending range).

    Steps:
      1. Plot a histogram of the "total_spend" column
         (plt.hist(df["total_spend"], bins=20)).
      2. Add a title ("The Trendiest — Customer Spending Distribution"),
         and axis labels ("Total Spend ($)", "Number of Customers").
      3. Call plt.tight_layout() so nothing gets cut off.

    Hint:
        plt.hist(df["total_spend"], bins=20)
    """
    # TODO: implement this function
    pass


def plot_top_customers(df, count=10):
    """
    Create a bar chart showing the top `count` customers by total_spend,
    from highest to lowest.

    Steps:
      1. Sort df by "total_spend" from highest to lowest.
      2. Take the top `count` rows.
      3. Plot it as a bar chart (plt.bar(...)) with customer_name on the
         x-axis and total_spend on the y-axis.
      4. Add a title ("The Trendiest — Top 10 Customers by Spend"), and
         axis labels ("Customer", "Total Spend ($)").
      5. Rotate the x-axis labels 45 degrees so they don't overlap:
         plt.xticks(rotation=45, ha="right")
      6. Call plt.tight_layout().

    Hint:
        top = df.sort_values("total_spend", ascending=False).head(count)
    """
    # TODO: implement this function
    pass
