"""
CHALLENGE PART 3 of 3: Save the Charts

Complete data_loader.py and visualise.py first. This file loads the
data, builds both charts, and saves them as image files so you (and your
teacher) can look at them.

Run it with:
    python main.py

Look for two new files afterwards: output/daily_revenue.png and
output/average_by_day_of_week.png
"""

import os
import matplotlib.pyplot as plt

from data_loader import load_daily_totals
from visualise import plot_daily_revenue, plot_average_by_day_of_week


def main():
    df = load_daily_totals()
    print(f"Loaded {len(df)} days of checkout totals.")

    os.makedirs("output", exist_ok=True)

    plt.figure()
    plot_daily_revenue(df)
    plt.savefig("output/daily_revenue.png")
    plt.close()
    print("Saved output/daily_revenue.png")

    plt.figure()
    plot_average_by_day_of_week(df)
    plt.savefig("output/average_by_day_of_week.png")
    plt.close()
    print("Saved output/average_by_day_of_week.png")

    # BONUS (optional, no TODO required): once your two charts above are
    # working, try adding a third chart of your own — maybe number of
    # transactions per day, or a 7-day rolling average of total_sales?
    # Add a new function to visualise.py and call it here the same way.


if __name__ == "__main__":
    main()
