"""
CHALLENGE PART 1 of 3: Load the Data

This project analyses several rounds of (pretend) game night scores from
The Trendiest, stored in tournament_scores.csv. It's split into 3 files:
    data_loader.py  - (this file) loads the CSV into a usable table
    visualise.py    - turns that table into charts
    main.py         - runs everything and saves the charts as images

tournament_scores.csv has these columns:
    round      - which round of game night this score is from (1, 2, 3...)
    player     - the player's name
    score      - the score they got that round
    game_type  - which game was being played that round, e.g. "Trivia Night"

YOUR TASK (this file)
----------------------
Use the pandas library to load the CSV file into a DataFrame (think of it
like a spreadsheet you can work with in code).
"""

import pandas as pd


def load_scores(csv_path="tournament_scores.csv"):
    """
    Read csv_path using pandas and return it as a DataFrame.

    Hint:
        return pd.read_csv(csv_path)
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    df = load_scores()
    print(df.head())  # show the first 5 rows
    print("\nColumn names:", list(df.columns))
    print("Total rows:", len(df))
