"""
CHALLENGE: Build InventoryItem and Inventory Classes
DIFFICULTY: Intermediate
FOLDER: 03-stock-management / tier3_intermediate

STORY
-----
The café wants each stockroom item to be its own self-contained "thing" in
the code (name, quantity, and its own low-stock threshold), and a single
Inventory that manages a whole collection of them — that's exactly what
classes are for.

YOUR TASK
---------
Complete the `InventoryItem` class and the `Inventory` class below by
implementing each method described in its docstring. Then test them using
the code at the bottom of the file.

EXAMPLE OUTPUT (from the test code at the bottom)
--------------------------------------------------
Restocked Coffee Beans by 10. New quantity: 22
Sold 25 units of Muffins. New quantity: 0
Sold 3 units of Napkins. New quantity: 2
Low stock items: ['Muffins', 'Napkins']
"""


class InventoryItem:
    """Represents one item tracked in the The Trendiest stockroom."""

    def __init__(self, name, quantity, low_stock_threshold):
        """
        Store name, quantity and low_stock_threshold on self, using
        exactly those attribute names (self.name, self.quantity,
        self.low_stock_threshold).
        """
        # TODO: implement this method
        pass

    def is_low(self):
        """Return True if self.quantity is at or below self.low_stock_threshold."""
        # TODO: implement this method
        pass


class Inventory:
    """Holds and manages multiple InventoryItem objects."""

    def __init__(self):
        """Set up an empty dictionary called self.items, mapping item name -> InventoryItem."""
        # TODO: implement this method
        pass

    def add_item(self, name, quantity, low_stock_threshold):
        """Create a new InventoryItem and store it in self.items, keyed by name."""
        # TODO: implement this method
        pass

    def restock(self, name, amount):
        """
        Increase the quantity of the item called name by amount.
        - If name isn't in self.items, print "{name} is not in the inventory."
        - Otherwise, print "Restocked {name} by {amount}. New quantity: {new_quantity}"
        """
        # TODO: implement this method
        pass

    def sell(self, name, amount):
        """
        Decrease the quantity of the item called name by amount, never
        letting it go below 0.
        - If name isn't in self.items, print "{name} is not in the inventory."
        - If amount is more than the current quantity, only remove what's
          available (quantity becomes 0) — don't go negative.
        - Print "Sold {amount} units of {name}. New quantity: {new_quantity}"
          (where new_quantity is whatever the quantity ended up as).
        """
        # TODO: implement this method
        pass

    def get_low_stock_items(self):
        """Return a list of names of every item where item.is_low() is True."""
        # TODO: implement this method
        pass


if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Coffee Beans", 12, low_stock_threshold=5)
    inventory.add_item("Muffins", 15, low_stock_threshold=5)
    inventory.add_item("Napkins", 5, low_stock_threshold=5)

    inventory.restock("Coffee Beans", 10)
    inventory.sell("Muffins", 25)
    inventory.sell("Napkins", 3)

    print(f"Low stock items: {inventory.get_low_stock_items()}")
