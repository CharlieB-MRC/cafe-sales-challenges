"""
CHALLENGE: Register New Customers
DIFFICULTY: Beginner
FOLDER: 04-customer-info / tier2_beginner

STORY
-----
It's loyalty card launch day! A line of customers wants to sign up at the
counter. You need to keep asking for a new customer's name and starting
points, adding each one to your records, until there's nobody left to
register.

YOUR TASK
---------
1. Keep asking "Customer name (or 'done' to finish): ".
2. If the answer is "done", stop asking.
3. Otherwise, also ask "Starting points: ", convert it to an int, and add
   a new dictionary like {"name": name, "points": points} to the
   customers list.
4. When the loop finishes, print how many customers were registered.

EXAMPLE OUTPUT
--------------
Customer name (or 'done' to finish): Priya
Starting points: 0
Registered Priya with 0 points.
Customer name (or 'done' to finish): Sam
Starting points: 20
Registered Sam with 20 points.
Customer name (or 'done' to finish): done
2 customers registered today.

HINTS
-----
- Use `while True:` and `break` to stop the loop when the customer types
  "done".
- Remember `int(...)` to convert the points input from text to a number.
- Use `customers.append({...})` to add a new customer dictionary to the
  list.
"""

customers = []

# TODO: write a while loop that:
#   - asks "Customer name (or 'done' to finish): "
#   - if the answer is "done", stops the loop
#   - otherwise asks "Starting points: ", converts it to an int, appends
#     a dictionary {"name": name, "points": points} to `customers`, and
#     prints "Registered {name} with {points} points."


# TODO: after the loop finishes, print how many customers were
# registered, e.g. "2 customers registered today."
