"""
CHALLENGE PART 2 of 3: Chart the Data

Complete data_loader.py first. This file turns the stock-levels DataFrame
into two charts using matplotlib.

YOUR TASK (this file)
----------------------
Implement both functions below. Each one should build a chart using
matplotlib and matplotlib's `savefig` should NOT be called here — that
happens in main.py. Just build the chart with plt (it will be shown or
saved by whoever calls these functions).
"""

import matplotlib.pyplot as plt


def plot_stock_depletion(df):
    """
    Create a line chart showing how EACH item's stock level changes over
    the month, with one line per item and a legend.

    Steps:
      1. Find every unique item name in df["item"].
      2. For each item, filter df down to just that item's rows, sorted
         by "date", and plot "date" on the x-axis and "stock_level" on
         the y-axis as a line (plt.plot(...)), using label=item so it
         shows up correctly in the legend.
      3. Add a title ("The Trendiest — Stock Depletion Over the Month"),
         and axis labels ("Date", "Stock Level").
      4. Call plt.legend() to show which line is which item.
      5. Rotate the x-axis labels 45 degrees so they don't overlap:
         plt.xticks(rotation=45, ha="right")
      6. Call plt.tight_layout() so nothing gets cut off.

    Hint:
        for item in df["item"].unique():
            item_df = df[df["item"] == item].sort_values("date")
            plt.plot(item_df["date"], item_df["stock_level"], label=item)
    """
    # TODO: implement this function
    pass


def plot_stockout_counts(df):
    """
    Create a bar chart showing how many times each item's stock level hit
    ZERO during the month (i.e. it completely ran out).

    Steps:
      1. Filter df down to only rows where stock_level == 0.
      2. Group those rows by "item" and count how many rows each item has
         (this is how many days that item was out of stock).
      3. Make sure EVERY item appears in the result, even ones that never
         hit zero (they should show a count of 0) — you can do this with
         `.reindex(df["item"].unique(), fill_value=0)` on the grouped
         result.
      4. Sort the result from highest to lowest.
      5. Plot it as a bar chart (plt.bar(...)) with items on the x-axis
         and the stockout count on the y-axis.
      6. Add a title ("The Trendiest — Days Fully Out of Stock"), and axis
         labels ("Item", "Number of Days at Zero Stock").
      7. Rotate the x-axis labels 45 degrees: plt.xticks(rotation=45, ha="right")
      8. Call plt.tight_layout().

    Hint:
        zero_days = df[df["stock_level"] == 0]
        counts = zero_days.groupby("item").size()
        counts = counts.reindex(df["item"].unique(), fill_value=0)
        counts = counts.sort_values(ascending=False)
    """
    # TODO: implement this function
    pass
