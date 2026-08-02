"""
CHALLENGE: Calculate the Change
DIFFICULTY: Beginner
FOLDER: 02-checkout-totals / tier2_beginner

STORY
-----
A customer walks up to the till with cash in hand. You need to ask how
much their item costs, ask how much cash they're handing over, and work
out their change — or politely tell them they haven't paid enough.

YOUR TASK
---------
1. Ask for the price of the item using input() (remember: input() always
   returns a string, so you'll need float() to convert it to a number).
2. Ask how much cash the customer paid, also converted to a float.
3. If the amount paid is less than the price, print a message saying they
   haven't paid enough and how much more they still owe.
4. Otherwise, calculate the change (amount paid - price) and print it.

EXAMPLE OUTPUT (price 4.50, customer pays 5.00)
------------------------------------------------
What is the price? $4.50
How much cash did the customer give you? $5.00
Change owed: $0.5

EXAMPLE OUTPUT (price 4.50, customer pays 4.00)
------------------------------------------------
What is the price? $4.50
How much cash did the customer give you? $4.00
Sorry, that's not enough. They still owe $0.5

HINTS
-----
- price = float(input("What is the price? $"))
- Use round(value, 2) if you want to avoid long decimals.
"""

# TODO 1: ask for the price using input(), convert it to a float,
#         and store it in a variable called price

# TODO 2: ask how much cash the customer paid, convert it to a float,
#         and store it in a variable called amount_paid

# TODO 3: if amount_paid is less than price, print:
#         "Sorry, that's not enough. They still owe ${amount they still owe}"
#         otherwise, calculate the change (amount_paid - price) and print:
#         "Change owed: ${change}"
