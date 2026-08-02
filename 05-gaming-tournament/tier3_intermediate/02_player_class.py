"""
CHALLENGE: Build a Player Class
DIFFICULTY: Intermediate
FOLDER: 05-gaming-tournament / tier3_intermediate

STORY
-----
The Trendiest wants each game-night regular to be their own self-contained
"thing" in the code, keeping track of every score they've ever posted —
that's exactly what a class is for.

YOUR TASK
---------
Complete the `Player` class below by implementing each method described
in its docstring. Then test it using the code at the bottom of the file.

EXAMPLE OUTPUT (from the test code at the bottom)
--------------------------------------------------
Priya's scores: [42, 37, 50]
Priya's average score: 43.0
Priya's best score: 50
"""


class Player:
    """Represents one game-night regular and their scores across games."""

    def __init__(self, name):
        """Store the player's name and set up an empty list of scores."""
        # TODO: create self.name (set to `name`) and self.scores (empty list)
        pass

    def add_score(self, score):
        """Add `score` to this player's list of scores."""
        # TODO: implement this method
        pass

    def average_score(self):
        """Return the mean of this player's scores, rounded to 1 decimal
        place. Return 0 if the player has no scores yet (avoid a
        divide-by-zero crash)."""
        # TODO: implement this method
        pass

    def best_score(self):
        """Return this player's highest score so far, or None if they
        have no scores yet."""
        # TODO: implement this method
        pass


if __name__ == "__main__":
    priya = Player("Priya")
    priya.add_score(42)
    priya.add_score(37)
    priya.add_score(50)

    print(f"Priya's scores: {priya.scores}")
    print(f"Priya's average score: {priya.average_score()}")
    print(f"Priya's best score: {priya.best_score()}")
