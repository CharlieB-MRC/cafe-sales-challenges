"""
CHALLENGE: Check for Low Stock
DIFFICULTY: Very, very easy
FOLDER: 03-stock-management / tier1_very_easy

STORY
-----
The café is running low on oat milk and nobody noticed until a customer
complained! The manager wants a quick check built into the system: compare
the current stock count of an item against its "low stock threshold" and
warn the staff if it's time to reorder.

YOUR TASK
---------
1. The variables below store the current stock count and the low stock
   threshold for Oat Milk (litres).
2. Write an if/else statement:
   - If current_stock is below low_stock_threshold, print a warning message.
   - Otherwise, print "Stock is fine".
Match the EXAMPLE OUTPUT exactly.

EXAMPLE OUTPUT (with the variables below, exactly as given)
-------------------------------------------------------------
Checking stock for: Oat Milk
Warning! Only 3 litres of Oat Milk left (threshold is 5).

HINT
----
An if/else statement looks like this:
    if some_number < another_number:
        print("...")
    else:
        print("...")
"""

item_name = "Oat Milk"
current_stock = 3
low_stock_threshold = 5

print(f"Checking stock for: {item_name}")

# TODO: write an if/else statement that:
#   - if current_stock is below low_stock_threshold, prints:
#     "Warning! Only {current_stock} litres of {item_name} left (threshold is {low_stock_threshold})."
#   - otherwise prints: "Stock is fine"
