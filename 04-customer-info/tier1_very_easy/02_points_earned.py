"""
CHALLENGE: Calculate Loyalty Points Earned
DIFFICULTY: Very, very easy
FOLDER: 04-customer-info / tier1_very_easy

STORY
-----
The Trendiest's loyalty scheme is simple: for every $10 a customer spends,
they earn 1 loyalty point (any leftover cents don't count). A customer
has just paid, and the till needs to work out how many points to add to
their card.

YOUR TASK
---------
The customer's total spend is already stored in the variable below.
1. Calculate how many points they earned, using the formula: 1 point per
   $10 spent, rounded DOWN to the nearest whole point. Store the result
   in a variable called points_earned.
2. Print a message showing how many points they earned, matching the
   EXAMPLE OUTPUT exactly.

EXAMPLE OUTPUT
--------------
(with total_spend = 47.50, exactly as given below)
You spent $47.5 and earned 4 loyalty points!

HINT
----
Use the // operator to divide and round down at the same time, then wrap
the result in int(...) so it prints as a whole number (47.50 // 10 gives
you 4.0, a float, and int(4.0) gives you 4):
    int(47.50 // 10)  ->  4
"""

total_spend = 47.50

# TODO 1: calculate points_earned using int(total_spend // 10), and store
# it in a variable called points_earned

# TODO 2: print a message matching the EXAMPLE OUTPUT, e.g.
# "You spent $47.5 and earned 4 loyalty points!"


print("\n(Check: does your output above match the EXAMPLE OUTPUT exactly?)")
