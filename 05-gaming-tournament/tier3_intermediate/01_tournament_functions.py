"""
CHALLENGE: Rebuild Score Tracking With Functions
DIFFICULTY: Intermediate
FOLDER: 05-gaming-tournament / tier3_intermediate

STORY
-----
Game night now runs across SEVERAL games per player (board games, arcade,
trivia), and the café wants the score-tracking logic cleaned up into
reusable functions instead of one long block of code.

YOUR TASK
---------
Implement the four functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom to register some players, record a few scores each, and print a
leaderboard and the overall winner.

EXAMPLE OUTPUT
--------------
----- LEADERBOARD (by average score) -----
1st: Priya - avg 39.5
2nd: Sam - avg 34.0
--------------------------------------------
Winner: Priya
"""

players = {}


def register_player(players, name):
    """
    Add `name` to the `players` dictionary with an empty list of scores,
    e.g. players["Priya"] = [].
    Do nothing if the player is already registered.
    """
    # TODO: implement this function
    pass


def record_score(players, name, score):
    """
    Append `score` to the list of scores for `name` in `players`.
    Assume the player has already been registered.

    Example:
        record_score(players, "Priya", 42)
        -> players["Priya"] becomes [42]
    """
    # TODO: implement this function
    pass


def get_leaderboard(players):
    """
    Return a list of (name, average_score) tuples, ranked from the
    highest average score to the lowest. average_score should be the
    mean of that player's scores list, rounded to 1 decimal place.

    Example:
        players = {"Priya": [42, 37], "Sam": [34]}
        get_leaderboard(players) -> [("Priya", 39.5), ("Sam", 34.0)]
    """
    # TODO: implement this function
    pass


def determine_winner(players):
    """
    Return the name of the player with the highest average score.
    Hint: you can reuse get_leaderboard() here — the winner is whoever
    is ranked first.
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    register_player(players, "Priya")
    register_player(players, "Sam")

    record_score(players, "Priya", 42)
    record_score(players, "Priya", 37)
    record_score(players, "Sam", 34)

    leaderboard = get_leaderboard(players)

    print("----- LEADERBOARD (by average score) -----")
    ordinals = ["1st", "2nd", "3rd", "4th", "5th"]
    for index, (name, avg) in enumerate(leaderboard):
        print(f"{ordinals[index]}: {name} - avg {avg}")
    print("--------------------------------------------")
    print(f"Winner: {determine_winner(players)}")
