"""
CHALLENGE: Rebuild Stock Management With Functions
DIFFICULTY: Intermediate
FOLDER: 03-stock-management / tier3_intermediate

STORY
-----
The stockroom system keeps getting messier every time someone adds a new
feature. The manager wants the logic cleaned up into proper reusable
functions, AND wants the stock counts to be remembered between runs — right
now, every time the program is closed, the stock resets, which isn't very
useful for a real café!

YOUR TASK
---------
Implement the four functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom. The stock dictionary should be loaded from stock_data.json at the
start (if the file exists) and saved back to it at the end, so the counts
persist between runs.

EXAMPLE OUTPUT (first ever run, stock_data.json does not exist yet)
---------------------------------------------------------------------
No saved stock file found — starting with default stock.
Added 10 units of Coffee Beans. New quantity: 22
Removed 5 units of Milk. New quantity: 15
Removed 100 units of Napkins — not enough stock! Still have 8.

----- STOCK REPORT -----
Coffee Beans        : 22
Milk                 : 15
Muffins              : 15
Napkins              : 8
-------------------------
Items needing reorder (5 or fewer): none

Stock saved to stock_data.json.

HINTS
-----
- Use `json.load(f)` to read a dictionary from a file, and `json.dump(data, f)`
  to write one.
- Use `os.path.exists(path)` to check if a file exists before loading it.
"""

import json
import os

DATA_FILE = "stock_data.json"

DEFAULT_STOCK = {
    "Coffee Beans": 12,
    "Milk": 20,
    "Muffins": 15,
    "Napkins": 8,
}


def load_stock():
    """
    If DATA_FILE exists, load and return the stock dictionary from it
    using json.load(). Otherwise, print "No saved stock file found —
    starting with default stock." and return a COPY of DEFAULT_STOCK
    (use DEFAULT_STOCK.copy() so the original never gets changed).
    """
    # TODO: implement this function
    pass


def add_stock(stock, item, amount):
    """
    Increase stock[item] by amount (if item isn't already a key, add it
    with a starting value of 0 first). Print
    "Added {amount} units of {item}. New quantity: {stock[item]}".
    """
    # TODO: implement this function
    pass


def remove_stock(stock, item, amount):
    """
    Decrease stock[item] by amount, but NEVER let it go below 0.
    - If item isn't in stock, print "{item} is not tracked in stock." and
      do nothing else.
    - If amount is more than the current stock for item, don't change the
      stock at all — print
      "Removed {amount} units of {item} — not enough stock! Still have {stock[item]}."
    - Otherwise, subtract amount and print
      "Removed {amount} units of {item}. New quantity: {stock[item]}".
    """
    # TODO: implement this function
    pass


def check_low_stock(stock, threshold):
    """
    Return a list of every item name in stock whose quantity is at or
    below threshold.
    """
    # TODO: implement this function
    pass


def generate_report(stock, threshold=5):
    """
    Print a formatted stock report, in the style shown in the EXAMPLE
    OUTPUT above:
      1. A header line "----- STOCK REPORT -----"
      2. One line per item: "{item:<20} : {quantity}" (use an f-string
         with a field width, e.g. f"{item:<20} : {quantity}")
      3. A footer line of dashes, e.g. "-------------------------"
      4. A line showing which items need reordering (use check_low_stock):
         "Items needing reorder ({threshold} or fewer): none" if the list
         is empty, otherwise
         "Items needing reorder ({threshold} or fewer): Item1, Item2"
    """
    # TODO: implement this function
    pass


def save_stock(stock):
    """
    Save the stock dictionary to DATA_FILE using json.dump(), then print
    "Stock saved to {DATA_FILE}."
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    stock = load_stock()

    add_stock(stock, "Coffee Beans", 10)
    remove_stock(stock, "Milk", 5)
    remove_stock(stock, "Napkins", 100)

    print()
    generate_report(stock)
    print()

    save_stock(stock)
