"""
CHALLENGE: Sell an Item and Update Stock
DIFFICULTY: Beginner
FOLDER: 03-stock-management / tier2_beginner

STORY
-----
Every time a barista sells something, the stockroom count needs to go down.
The café wants a quick tool at the counter: type in what was just sold and
how many, and it updates the stock straight away — but it should never let
stock go below zero (that would mean selling ingredients you don't have!).

YOUR TASK
---------
1. The STOCK dictionary below stores each item name and how many units are
   currently on the shelf.
2. Ask which item was just used (sold), using input(), and store the answer
   in a variable called item_name.
3. Ask how many units were sold, using input(), and convert it to an int.
4. Check whether item_name exists in STOCK.
   - If it doesn't exist, print a "we don't stock that" message.
   - If it exists but there isn't enough stock (amount > current stock),
     print an error and REFUSE to update the stock.
   - Otherwise, subtract amount from STOCK[item_name] and print the new
     quantity.

EXAMPLE OUTPUT (item_name="Coffee Beans", amount sold = "4")
--------------------------------------------------------------
Which item was just used? Coffee Beans
How many units? 4
Coffee Beans stock updated. New quantity: 8

EXAMPLE OUTPUT (item_name="Coffee Beans", amount sold = "100")
------------------------------------------------------------------
Which item was just used? Coffee Beans
How many units? 100
Sorry, only 12 units of Coffee Beans in stock — can't remove 100.

EXAMPLE OUTPUT (item_name="Pizza", amount sold = "1")
--------------------------------------------------------
Which item was just used? Pizza
How many units? 1
We don't stock Pizza.

HINTS
-----
- Use `item_name in STOCK` to check if a key exists in a dictionary.
- Use `int(input(...))` to read a whole number from the user.
"""

STOCK = {
    "Coffee Beans": 12,
    "Milk": 20,
    "Muffins": 15,
    "Napkins": 8,
}

# TODO 1: ask "Which item was just used? " with input(), store in item_name

# TODO 2: ask "How many units? " with input(), convert to int, store in amount

# TODO 3: check whether item_name exists in STOCK
#   - if it doesn't: print "We don't stock {item_name}."
#   - if it does but amount is more than STOCK[item_name]: print
#     "Sorry, only {STOCK[item_name]} units of {item_name} in stock — can't remove {amount}."
#   - otherwise: subtract amount from STOCK[item_name] and print
#     "{item_name} stock updated. New quantity: {STOCK[item_name]}"
