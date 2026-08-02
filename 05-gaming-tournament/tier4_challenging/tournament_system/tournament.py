"""
CHALLENGE PART 2 of 3: The Tournament

See player.py for an overview of this whole project. Complete player.py
first, since this file needs it.

YOUR TASK (this file)
----------------------
Build a Tournament class that runs a simple SINGLE-ELIMINATION bracket:
    - It starts with a list of Player objects (must be a power of 2:
      2, 4, 8, ... players — you can assume the input is always valid).
    - Each round, players are paired up in the order they appear in the
      current round's list: (player[0] vs player[1]), (player[2] vs
      player[3]), and so on.
    - For each match, you're given the two players' scores for that round
      (via play_round()). Whoever scores higher in a match advances to
      the next round and has that score added to their own total via
      add_round_score(). The loser is knocked out.
    - This repeats until only one player remains: the champion.
    - Results (every match played) can be saved to a CSV file.
"""

import csv

from player import Player


class Tournament:
    """Runs a single-elimination tournament between Player objects."""

    def __init__(self, players):
        """
        Store the starting list of Player objects as self.players (the
        players still in the tournament — this list shrinks each round),
        set self.round_number to 1, and set up an empty list called
        self.match_history to record every match played (as dictionaries).
        """
        # TODO: implement this method
        pass

    def play_round(self, scores):
        """
        Play one round of the bracket.

        `scores` is a list of scores, IN THE SAME ORDER as self.players,
        one score per player for this round (e.g. if self.players is
        [Priya, Sam, Mia, Leo], scores might be [42, 37, 50, 25] meaning
        Priya scored 42, Sam scored 37, Mia scored 50, Leo scored 25).

        Steps:
          1. Pair up players two at a time in order: (0,1), (2,3), ...
          2. For each pair, work out who scored higher (assume no ties —
             you can assume scores are always different within a match).
          3. Call winner.add_round_score(winner's score).
          4. Append a dictionary to self.match_history describing the
             match, e.g.:
                 {"round": self.round_number, "player_1": p1.name,
                  "player_1_score": s1, "player_2": p2.name,
                  "player_2_score": s2, "winner": winner.name}
          5. Build a new list of the winners only (in the order their
             matches were played) and set self.players to that new list.
          6. Increase self.round_number by 1.

        Hint: use zip(self.players, scores) to pair each player with
        their score for this round, then step through that paired list
        two players at a time (index 0 and 1 together, 2 and 3 together...).
        """
        # TODO: implement this method
        pass

    def is_finished(self):
        """Return True if only one player remains in self.players."""
        # TODO: implement this method
        pass

    def get_champion(self):
        """
        Return the single remaining Player if the tournament is finished,
        otherwise return None.
        """
        # TODO: implement this method
        pass

    def save_results(self, csv_path="results.csv"):
        """
        Write self.match_history to a CSV file at csv_path, with columns:
        round, player_1, player_1_score, player_2, player_2_score, winner

        Hint:
            with open(csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=[...])
                writer.writeheader()
                writer.writerows(self.match_history)
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    # Quick manual check while you're building this file: a 4-player
    # tournament played over 2 rounds.
    players = [Player("Priya"), Player("Sam"), Player("Mia"), Player("Leo")]
    t = Tournament(players)

    t.play_round([42, 37, 50, 25])   # Priya beats Sam, Mia beats Leo
    print("Round 1 winners:", t.players)

    t.play_round([60, 55])           # Priya beats Mia
    print("Finished?", t.is_finished())
    print("Champion:", t.get_champion())

    t.save_results("results.csv")
    print("Saved results.csv")
