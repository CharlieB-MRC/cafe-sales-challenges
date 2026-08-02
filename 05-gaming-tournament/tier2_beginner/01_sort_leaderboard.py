"""
CHALLENGE: Sort the Leaderboard
DIFFICULTY: Beginner
FOLDER: 05-gaming-tournament / tier2_beginner

STORY
-----
Game night scores have been scribbled down in the order players finished
their game, NOT in ranked order. Before you can print a proper leaderboard,
you need to sort the list from highest score to lowest.

YOUR TASK
---------
1. SCORES below is a list of (name, score) tuples, in no particular order.
2. Use Python's sorted() with a key= to sort them from highest score to
   lowest.
3. Loop over the sorted list and print a ranked leaderboard, exactly like
   the example output (1st, 2nd, 3rd, 4th, ...).

EXAMPLE OUTPUT
--------------
1st: Priya - 42 pts
2nd: Sam - 37 pts
3rd: Mia - 30 pts
4th: Leo - 25 pts

HINTS
-----
- sorted() takes a key= function that tells it what to sort by. For a
  tuple like ("Priya", 42), the score is item[1]:
      sorted(SCORES, key=lambda item: item[1], reverse=True)
  (reverse=True sorts highest first instead of lowest first.)
- You'll need to work out the right ordinal word (1st, 2nd, 3rd, 4th, ...)
  for each position. For this challenge, a simple list of ordinal suffixes
  like ["1st", "2nd", "3rd", "4th"] is fine since we only ever have a
  handful of players.
"""

SCORES = [
    ("Leo", 25),
    ("Priya", 42),
    ("Mia", 30),
    ("Sam", 37),
]

ORDINALS = ["1st", "2nd", "3rd", "4th", "5th", "6th"]

# TODO 1: use sorted() with a key= (and reverse=True) to sort SCORES from
#         highest score to lowest. Store the result in a new variable,
#         e.g. ranked_scores.

# TODO 2: loop over ranked_scores using enumerate() so you know each
#         player's position (index 0 = 1st place, index 1 = 2nd place...)
#         and print "{ordinal}: {name} - {score} pts" for each one, using
#         ORDINALS[index] to get the right ordinal word.
