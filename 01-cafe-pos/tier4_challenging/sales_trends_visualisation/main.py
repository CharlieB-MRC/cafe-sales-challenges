"""
CHALLENGE PART 3 of 3: Save the Charts

Complete data_loader.py and visualise.py first. This file loads the data,
builds both charts, and saves them as image files so you (and your
teacher) can look at them.

Run it with:
    python main.py

Look for two new files afterwards: best_sellers.png and revenue_by_hour.png
"""

import os
import matplotlib.pyplot as plt

from data_loader import load_sales
from visualise import plot_best_sellers, plot_revenue_by_hour


def main():
    df = load_sales()
    print(f"Loaded {len(df)} sales records.")

    os.makedirs("output", exist_ok=True)

    plt.figure()
    plot_best_sellers(df)
    plt.savefig("output/best_sellers.png")
    plt.close()
    print("Saved output/best_sellers.png")

    plt.figure()
    plot_revenue_by_hour(df)
    plt.savefig("output/revenue_by_hour.png")
    plt.close()
    print("Saved output/revenue_by_hour.png")

    # BONUS (optional, no TODO required): once your two charts above are
    # working, try adding a third chart of your own — maybe total revenue
    # by day of the week? Add a new function to visualise.py and call it
    # here the same way.


if __name__ == "__main__":
    main()
