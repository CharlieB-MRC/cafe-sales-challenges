"""
CHALLENGE PART 1 of 4: The Inventory

This project (inventory_system) is split across several files that work
together:
    inventory_data.csv - the raw stock data (already provided, don't edit)
    inventory.py        - (this file) loads/saves stock and holds items
    alerts.py            - checks for low stock and builds warning messages
    reorder.py           - works out how much to reorder from the supplier
    main.py              - runs the whole program
    test_inventory_system.py - automated checks for your code

Work through them in that order. Run `pytest` at any point to see which
parts are passing.

YOUR TASK (this file)
----------------------
Build an Inventory class that loads its data from inventory_data.csv (a
row per item, with columns: name, quantity, low_stock_threshold,
target_stock) and can save itself back to CSV.
"""

import csv

FIELDNAMES = ["name", "quantity", "low_stock_threshold", "target_stock"]


class InventoryItem:
    """One tracked stockroom item."""

    def __init__(self, name, quantity, low_stock_threshold, target_stock):
        self.name = name
        self.quantity = int(quantity)
        self.low_stock_threshold = int(low_stock_threshold)
        self.target_stock = int(target_stock)

    def is_low(self):
        """Return True if quantity is at or below low_stock_threshold."""
        return self.quantity <= self.low_stock_threshold


class Inventory:
    """Loads, stores, and saves a collection of InventoryItems."""

    def __init__(self, data_path="inventory_data.csv"):
        """
        Store data_path on self, then set up self.items as an empty
        dictionary of {name: InventoryItem}, and call self.load() to
        populate it.
        """
        # TODO: implement this method
        pass

    def load(self):
        """
        Read self.data_path as a CSV file using csv.DictReader and create
        an InventoryItem for every row, storing each one in self.items
        keyed by its name.

        Hint:
            with open(self.data_path, newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    item = InventoryItem(
                        row["name"], row["quantity"],
                        row["low_stock_threshold"], row["target_stock"]
                    )
                    self.items[item.name] = item
        """
        # TODO: implement this method
        pass

    def save(self, data_path=None):
        """
        Write every item in self.items back out to CSV (to data_path if
        given, otherwise self.data_path), using csv.DictWriter with
        FIELDNAMES as the header row. Each row should have the item's
        name, quantity, low_stock_threshold and target_stock.
        """
        # TODO: implement this method
        pass

    def get_item(self, name):
        """Return the InventoryItem called name, or None if it doesn't exist."""
        # TODO: implement this method
        pass

    def restock(self, name, amount):
        """
        Increase the quantity of item `name` by amount.
        - If the item doesn't exist, print "{name} is not in the inventory."
        - Otherwise increase its quantity and print
          "Restocked {name} by {amount}. New quantity: {new_quantity}"
        """
        # TODO: implement this method
        pass

    def sell(self, name, amount):
        """
        Decrease the quantity of item `name` by amount, never letting it
        go below 0 (if amount is more than available, quantity becomes 0).
        - If the item doesn't exist, print "{name} is not in the inventory."
        - Otherwise print "Sold {amount} units of {name}. New quantity: {new_quantity}"
        """
        # TODO: implement this method
        pass

    def list_items(self):
        """Return a list of every item name in self.items."""
        # TODO: implement this method
        pass


if __name__ == "__main__":
    # Quick manual check while you're building this file.
    inv = Inventory()
    print("Items loaded:", inv.list_items())
    print("Coffee Beans quantity:", inv.get_item("Coffee Beans").quantity)
