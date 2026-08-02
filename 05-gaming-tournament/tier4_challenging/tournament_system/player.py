"""
CHALLENGE PART 1 of 3: The Player

This project (tournament_system) is split across several files that work
together:
    player.py     - (this file) represents one tournament competitor
    tournament.py - runs a single-elimination bracket between players
    main.py        - runs the whole program
    results.csv    - created automatically when main.py runs (don't create
                     this yourself — it appears after you run main.py)
    test_tournament_system.py - automated checks for your code

Work through them in that order. Run `pytest` at any point to see which
parts are passing.

YOUR TASK (this file)
----------------------
Complete the Player class so it can hold a name and a running list of the
scores it gets across each round of the tournament.
"""


class Player:
    """Represents one competitor in the The Trendiest game night tournament."""

    def __init__(self, name):
        """
        Store the player's name and set up an empty list (self.scores) to
        record the score they get in each round they play.
        """
        # TODO: implement this method
        pass

    def add_round_score(self, score):
        """Record `score` as this player's result for a round."""
        # TODO: implement this method
        pass

    def total_score(self):
        """Return the sum of every score this player has recorded so far."""
        # TODO: implement this method
        pass

    def __repr__(self):
        """
        Return a helpful text representation, e.g. "Player(Priya)".
        This one is done for you — it's used by print() and by the tests.
        """
        return f"Player({self.name})"


if __name__ == "__main__":
    # Quick manual check while you're building this file.
    p = Player("Priya")
    p.add_round_score(42)
    p.add_round_score(37)
    print(p)
    print("Total score:", p.total_score())
