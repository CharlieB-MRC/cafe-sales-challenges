"""
CHALLENGE PART 2 of 3: Chart the Data

Complete data_loader.py first. This file turns the scores DataFrame into
two charts using matplotlib.

YOUR TASK (this file)
----------------------
Implement both functions below. Each one should build a chart using
matplotlib and matplotlib's `savefig` should NOT be called here — that
happens in main.py. Just build the chart with plt (it will be shown or
saved by whoever calls these functions).
"""

import matplotlib.pyplot as plt


def plot_score_progression(df):
    """
    Create a line chart showing each player's score across rounds, with
    one line per player and a legend.

    Steps:
      1. Find the unique player names in df["player"].
      2. For each player, filter df to just their rows, sort by "round"
         (ascending), and plot "round" on the x-axis against "score" on
         the y-axis as a line (use plt.plot(..., label=player) so the
         legend can show each player's name).
      3. Add a title ("The Trendiest Game Night — Score Progression"), axis
         labels ("Round", "Score"), and a legend (plt.legend()).
      4. Call plt.tight_layout().

    Hint:
        for player in df["player"].unique():
            player_df = df[df["player"] == player].sort_values("round")
            plt.plot(player_df["round"], player_df["score"], label=player)
    """
    # TODO: implement this function
    pass


def plot_total_wins(df):
    """
    Create a bar chart showing the total number of ROUNDS WON by each
    player. A player "wins" a round if they had the highest score of
    all players in that round.

    Steps:
      1. For each round number in df["round"].unique(), find the row
         with the highest score in that round (its "player" is that
         round's winner). One way: group by "round" and use idxmax() on
         "score" to get the winning row's index, then look up df["player"]
         at those indexes.
      2. Count how many rounds each player won.
      3. Plot the win counts as a bar chart (plt.bar(...)), one bar per
         player, from most wins to fewest.
      4. Add a title ("The Trendiest Game Night — Total Round Wins"), and
         axis labels ("Player", "Rounds Won").
      5. Call plt.tight_layout().

    Hint:
        winning_rows = df.loc[df.groupby("round")["score"].idxmax()]
        win_counts = winning_rows["player"].value_counts()
    """
    # TODO: implement this function
    pass
