"""
CHALLENGE PART 2 of 4: Low Stock Alerts

See inventory.py for an overview of this whole project. Complete
inventory.py first, since this file needs it.

YOUR TASK (this file)
----------------------
Write functions that check an Inventory for low-stock items and turn them
into friendly warning messages the café manager can read at a glance.
"""

from inventory import Inventory


def get_low_stock_items(inventory: Inventory):
    """
    Return a list of InventoryItem objects (not just names!) from
    inventory.items where item.is_low() is True.
    """
    # TODO: implement this function
    pass


def build_alert_messages(inventory: Inventory):
    """
    Use get_low_stock_items() to find every low-stock item, and return a
    list of warning message strings, one per low item, in this exact
    format:
        "LOW STOCK: {name} has {quantity} left (threshold is {low_stock_threshold})."

    If there are no low-stock items, return an empty list.
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    inv = Inventory()
    for message in build_alert_messages(inv):
        print(message)
