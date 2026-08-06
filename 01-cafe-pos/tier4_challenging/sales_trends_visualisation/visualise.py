"""
CHALLENGE PART 2 of 3: Chart the Data

Complete data_loader.py first. This file turns the sales DataFrame into
two charts using matplotlib.

YOUR TASK (this file)
----------------------
Implement both functions below. Each one should build a chart using
matplotlib and matplotlib's `savefig` should NOT be called here — that
happens in main.py. Just build the chart with plt (it will be shown or
saved by whoever calls these functions).
"""

import matplotlib.pyplot as plt


def plot_best_sellers(df):
    """
    Create a bar chart showing total quantity sold for each item, from
    most to least popular.

    Steps:
      1. Group df by "item" and sum the "quantity" column.
      2. Sort the result from highest to lowest.
      3. Plot it as a bar chart (plt.bar(...)) with items on the x-axis
         and total quantity on the y-axis.
      4. Add a title ("The Trendiest — Best Sellers This Week"), and axis
         labels ("Item", "Total Quantity Sold").
      5. Rotate the x-axis labels 45 degrees so they don't overlap:
         plt.xticks(rotation=45, ha="right")
      6. Call plt.tight_layout() so nothing gets cut off.

    Hint:
        totals = df.groupby("item")["quantity"].sum().sort_values(ascending=False)
    """
    


def plot_revenue_by_hour(df):
    """
    Create a line chart showing total revenue for each hour of the day
    (across the whole week combined), so the café can see its busiest
    times.

    Steps:
      1. Group df by "hour" and sum the "revenue" column.
      2. Sort by hour (ascending, so the line reads left-to-right in
         time order).
      3. Plot it as a line chart (plt.plot(...)).
      4. Add a title ("The Trendiest — Revenue by Hour of Day"), and axis
         labels ("Hour", "Total Revenue ($)").
      5. Call plt.tight_layout().
    """
    # TODO: implement this function
    pass
