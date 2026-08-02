"""
CHALLENGE: Look Up a Customer by ID
DIFFICULTY: Beginner
FOLDER: 04-customer-info / tier2_beginner

STORY
-----
A customer taps their loyalty card at the counter. The card only stores a
short customer ID, so the till needs to look that ID up in the customer
records and show the barista who it belongs to and how many points they
have.

YOUR TASK
---------
1. The CUSTOMERS dictionary below stores customer info, keyed by ID.
2. Ask for a customer ID using input().
3. Check whether that ID exists in CUSTOMERS.
   - If it does, print their name and points using the format shown in
     the example.
   - If it doesn't, print "Customer not found."

EXAMPLE OUTPUT (customer types "C002")
---------------------------------------
Enter customer ID: C002
Sam Tran - 85 points

EXAMPLE OUTPUT (customer types "C999")
---------------------------------------
Enter customer ID: C999
Customer not found.

HINTS
-----
- Use `customer_id in CUSTOMERS` to check if a key exists in a dictionary.
- Use `CUSTOMERS[customer_id]` to get the matching inner dictionary once
  you know it exists, then use ["name"] and ["points"] on that.
"""

CUSTOMERS = {
    "C001": {"name": "Priya Nair", "points": 120},
    "C002": {"name": "Sam Tran", "points": 85},
    "C003": {"name": "Jordan Lee", "points": 260},
    "C004": {"name": "Aaliyah Brown", "points": 40},
}

# TODO 1: ask for a customer ID using input(), and store their answer in
#         a variable called customer_id

# TODO 2: check whether customer_id exists in CUSTOMERS
#         - if it does: print "{name} - {points} points"
#         - if it doesn't: print "Customer not found."
