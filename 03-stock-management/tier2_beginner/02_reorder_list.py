"""
CHALLENGE: Build the Reorder List
DIFFICULTY: Beginner
FOLDER: 03-stock-management / tier2_beginner

STORY
-----
Once a week, the café manager needs a list of every stockroom item that's
running low, so they know exactly what to order from the supplier. Anything
at or below 5 units needs reordering.

YOUR TASK
---------
1. The STOCK dictionary below stores each item name and how many units are
   currently on the shelf.
2. Loop through STOCK and build a list called needs_reordering containing
   the name of every item whose quantity is at or below THRESHOLD.
3. Print the reorder list, matching the EXAMPLE OUTPUT below exactly.

EXAMPLE OUTPUT (with the STOCK dictionary below, exactly as given)
----------------------------------------------------------------------
Items that need reordering (5 units or fewer):
- Napkins
- Tea Bags
- Sugar Sachets

HINTS
-----
- Start with `needs_reordering = []` before the loop.
- Loop over the dictionary like this: `for item, quantity in STOCK.items():`
- Use `.append(...)` to add an item name to the list.
- To print each item on its own line with a "- " prefix, loop over the
  list again with a `for` loop.
"""

STOCK = {
    "Coffee Beans": 12,
    "Milk": 20,
    "Muffins": 15,
    "Napkins": 4,
    "Tea Bags": 5,
    "Sugar Sachets": 2,
    "Cups": 30,
}

THRESHOLD = 5

# TODO 1: create an empty list called needs_reordering

# TODO 2: loop through STOCK.items() and, for every item whose quantity is
#         at or below THRESHOLD, append its name to needs_reordering

# TODO 3: print "Items that need reordering ({THRESHOLD} units or fewer):"
#         then loop over needs_reordering and print "- {item}" for each one
