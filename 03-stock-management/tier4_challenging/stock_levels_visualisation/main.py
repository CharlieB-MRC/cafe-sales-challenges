"""
CHALLENGE PART 3 of 3: Save the Charts

Complete data_loader.py and visualise.py first. This file loads the data,
builds both charts, and saves them as image files so you (and your
teacher) can look at them.

Run it with:
    python main.py

Look for two new files afterwards: stock_depletion.png and stockout_counts.png
"""

import os
import matplotlib.pyplot as plt

from data_loader import load_stock_levels
from visualise import plot_stock_depletion, plot_stockout_counts


def main():
    df = load_stock_levels()
    print(f"Loaded {len(df)} stock-level readings.")

    os.makedirs("output", exist_ok=True)

    plt.figure()
    plot_stock_depletion(df)
    plt.savefig("output/stock_depletion.png")
    plt.close()
    print("Saved output/stock_depletion.png")

    plt.figure()
    plot_stockout_counts(df)
    plt.savefig("output/stockout_counts.png")
    plt.close()
    print("Saved output/stockout_counts.png")

    # BONUS (optional, no TODO required): once your two charts above are
    # working, try adding a third chart of your own — maybe average daily
    # stock level per item? Add a new function to visualise.py and call it
    # here the same way.


if __name__ == "__main__":
    main()
