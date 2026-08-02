"""
CHALLENGE PART 3 of 3: Save the Charts

Complete data_loader.py and visualise.py first. This file loads the data,
builds both charts, and saves them as image files so you (and your
teacher) can look at them.

Run it with:
    python main.py

Look for two new files afterwards: score_progression.png and total_wins.png
"""

import os
import matplotlib.pyplot as plt

from data_loader import load_scores
from visualise import plot_score_progression, plot_total_wins


def main():
    df = load_scores()
    print(f"Loaded {len(df)} score records.")

    os.makedirs("output", exist_ok=True)

    plt.figure()
    plot_score_progression(df)
    plt.savefig("output/score_progression.png")
    plt.close()
    print("Saved output/score_progression.png")

    plt.figure()
    plot_total_wins(df)
    plt.savefig("output/total_wins.png")
    plt.close()
    print("Saved output/total_wins.png")

    # BONUS (optional, no TODO required): once your two charts above are
    # working, try adding a third chart of your own — maybe average score
    # by game_type? Add a new function to visualise.py and call it here
    # the same way.


if __name__ == "__main__":
    main()
