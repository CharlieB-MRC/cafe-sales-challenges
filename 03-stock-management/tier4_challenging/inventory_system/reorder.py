"""
CHALLENGE PART 3 of 4: Supplier Reorder Calculator

See inventory.py for an overview of this whole project. Complete
inventory.py and alerts.py first, since this file needs both.

YOUR TASK (this file)
----------------------
Write a function that looks at every low-stock item and works out how
many units to order from the supplier to bring it back up to its
target_stock level.

EXAMPLE OUTPUT (for Napkins: quantity=8, target_stock=25, low_stock_threshold=10)
------------------------------------------------------------------------------------
{"Napkins": 17}
(because 25 - 8 = 17 units are needed to reach the target)
"""

from inventory import Inventory
from alerts import get_low_stock_items


def calculate_reorder_amounts(inventory: Inventory):
    """
    Build and return a dictionary of {item_name: amount_to_order} for
    every low-stock item in inventory (use get_low_stock_items()).

    For each low item, the amount to order is:
        item.target_stock - item.quantity
    (This will always be a positive number since low items are always
    below their threshold, which is always below their target_stock.)
    """
    # TODO: implement this function
    pass


def print_reorder_summary(inventory: Inventory):
    """
    Call calculate_reorder_amounts() and print a formatted summary:
      1. Header line: "----- SUPPLIER REORDER SUMMARY -----"
      2. One line per item to reorder: "{name}: order {amount} units"
      3. If there's nothing to reorder, print "Nothing to reorder — all
         stock levels are healthy." instead of the per-item lines.
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    inv = Inventory()
    print_reorder_summary(inv)
