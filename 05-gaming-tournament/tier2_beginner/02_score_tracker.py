"""
CHALLENGE: Live Score Tracker
DIFFICULTY: Beginner
FOLDER: 05-gaming-tournament / tier2_beginner

STORY
-----
Game night is in full swing and players keep coming up to the counter to
report their scores from the arcade cabinet. You need a little program
that keeps taking scores until everyone's finished, then reports the
highest score and the average score of the night.

YOUR TASK
---------
1. Keep asking for a player's name using input(). If they type "done",
   stop asking.
2. Otherwise, also ask for that player's score (convert it to an int!).
3. Store each (name, score) pair in a list.
4. When "done" is typed, print the highest score (with the player's name)
   and the average score, rounded to 1 decimal place.

EXAMPLE OUTPUT
--------------
Player name (or 'done' to finish): Priya
Score for Priya: 42
Player name (or 'done' to finish): Sam
Score for Sam: 37
Player name (or 'done' to finish): done

Highest score: Priya with 42 pts
Average score: 39.5

HINTS
-----
- Use a `while True:` loop, and `break` when the name typed is "done".
- Keep a list like `results = []` outside the loop, and append a
  (name, score) tuple to it inside the loop.
- To find the highest score, you can loop over `results` and keep track
  of the best one seen so far, or use `max(results, key=lambda r: r[1])`.
- For the average: sum up all the scores and divide by how many there are.
"""

results = []

# TODO: write a while loop that:
#   - asks "Player name (or 'done' to finish): "
#   - if the answer is "done", stops the loop
#   - otherwise asks "Score for {name}: ", converts the answer to an int,
#     and appends (name, score) to `results`


# TODO: after the loop finishes, work out and print:
#   - the highest score and which player got it, e.g.
#     "Highest score: Priya with 42 pts"
#   - the average score of everyone in `results`, rounded to 1 decimal
#     place, e.g. "Average score: 39.5"
