"""
CHALLENGE: Manage Customers With Functions and a JSON File
DIFFICULTY: Intermediate
FOLDER: 04-customer-info / tier3_intermediate

STORY
-----
The café's loyalty records currently vanish every time the till program
closes — not great! The head barista wants the customer list saved to a
file so it's still there tomorrow morning. You'll organise the logic into
functions and persist everything to customers.json.

YOUR TASK
---------
Implement the three functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom:
  1. Load customers from customers.json if it already exists, otherwise
     start with an empty list.
  2. Register a couple of new customers and add some points to one of
     them.
  3. Print the top customer.
  4. Save the updated customers list back to customers.json.

EXAMPLE OUTPUT (on the very first run, when customers.json doesn't exist)
---------------------------------------------------------------------------
Registered Priya with 0 points.
Registered Sam with 0 points.
Added 50 points to Priya.
Top customer: Priya with 50 points
Saved 2 customers to customers.json.

HINTS
-----
- Use `os.path.exists("customers.json")` to check if the file is there.
- Use `json.load(f)` to read and `json.dump(data, f)` to write.
- Each customer can be a dictionary like {"name": ..., "points": ...}.
"""

import json
import os

DATA_FILE = "customers.json"


def register_customer(customers, name):
    """
    Add a new customer dictionary {"name": name, "points": 0} to the
    `customers` list, then print "Registered {name} with 0 points."

    Example:
        register_customer([], "Priya")
        -> customers is now [{"name": "Priya", "points": 0}]
    """
    # TODO: implement this function
    pass


def add_points(customers, name, amount):
    """
    Find the customer in `customers` whose "name" matches `name`, and add
    `amount` to their "points". Print "Added {amount} points to {name}."
    If no customer with that name is found, print
    "Customer {name} not found." instead.
    """
    # TODO: implement this function
    pass


def find_top_customer(customers):
    """
    Return the customer dictionary (from `customers`) with the highest
    "points" value. Return None if `customers` is empty.

    Example:
        find_top_customer([{"name": "A", "points": 5},
                            {"name": "B", "points": 20}])
        -> {"name": "B", "points": 20}
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    # TODO 1: load customers from DATA_FILE if it exists (use json.load),
    # otherwise start with customers = []

    customers = []  # replace this line with your loading logic above

    register_customer(customers, "Priya")
    register_customer(customers, "Sam")
    add_points(customers, "Priya", 50)

    top = find_top_customer(customers)
    print(f"Top customer: {top['name']} with {top['points']} points")

    # TODO 2: save `customers` back to DATA_FILE (use json.dump), then
    # print "Saved {len(customers)} customers to customers.json."
