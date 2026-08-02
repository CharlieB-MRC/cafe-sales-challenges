"""
CHALLENGE PART 3 of 3: Save the Charts

Complete data_loader.py and visualise.py first. This file loads the data,
builds both charts, and saves them as image files so you (and your
teacher) can look at them.

Run it with:
    python main.py

Look for two new files afterwards: output/spend_distribution.png and
output/top_customers.png
"""

import os
import matplotlib.pyplot as plt

from data_loader import load_customers
from visualise import plot_spend_distribution, plot_top_customers


def main():
    df = load_customers()
    print(f"Loaded {len(df)} customer records.")

    os.makedirs("output", exist_ok=True)

    plt.figure()
    plot_spend_distribution(df)
    plt.savefig("output/spend_distribution.png")
    plt.close()
    print("Saved output/spend_distribution.png")

    plt.figure()
    plot_top_customers(df)
    plt.savefig("output/top_customers.png")
    plt.close()
    print("Saved output/top_customers.png")

    # BONUS (optional, no TODO required): once your two charts above are
    # working, try adding a third chart of your own — maybe average
    # spend per loyalty tier? Add a new function to visualise.py and
    # call it here the same way.


if __name__ == "__main__":
    main()
