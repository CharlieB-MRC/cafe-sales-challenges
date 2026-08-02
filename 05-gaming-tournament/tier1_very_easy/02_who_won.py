"""
CHALLENGE: Who Won the Round?
DIFFICULTY: Very, very easy
FOLDER: 05-gaming-tournament / tier1_very_easy

STORY
-----
Two customers just finished a round of the café's arcade cabinet during
game night. The high-score display is broken, so you need to work out
(and announce) who won using Python instead.

YOUR TASK
---------
Using the variables already provided below, work out who scored higher
and print the correct message using if/elif/else. There's ONE block of
TODOs to fill in.

EXAMPLE OUTPUT (with the variables below, exactly as given)
-------------------------------------------------------------
Jordan scored 58. Casey scored 61.
Casey wins this round!

HINT
----
Compare the two score variables with if/elif/else:
    if score_a > score_b:
        ...
    elif score_b > score_a:
        ...
    else:
        ...  # it's a tie
"""

player_a_name = "Jordan"
player_a_score = 58
player_b_name = "Casey"
player_b_score = 61

print(f"{player_a_name} scored {player_a_score}. {player_b_name} scored {player_b_score}.")

# TODO: use if/elif/else to compare player_a_score and player_b_score, then
# print ONE of these three lines (fill in the right names):
#   "{winner_name} wins this round!"        <- if one score is higher
#   "It's a tie!"                            <- if the scores are equal


print("\n(Check: does your output above match the EXAMPLE OUTPUT exactly?)")
