"""
CHALLENGE PART 3 of 4: Putting It All Together

Complete cart.py and checkout.py first. This file ties them all together
into a program you can actually run, and also writes the final receipt
out to a .txt file (so it could be "printed" for a real customer).

YOUR TASK
---------
Write a loop that:
  1. Creates a Cart.
  2. Repeatedly asks the barista what item (and how many) to add, until
     they type "done".
  3. Asks whether the customer is a loyalty member (y/n) and whether
     they have a voucher code (leave blank for none).
  4. Builds a Checkout, prints the receipt, and also saves it to
     receipt.txt in this same folder.

Run it with:
    python main.py
"""

from cart import Cart, load_menu
from checkout import Checkout


def main():
    menu = load_menu()
    cart = Cart(menu)

    print("The Trendiest Checkout — type an item name to add it, or 'done' to finish.")
    print("Available items:", ", ".join(menu.keys()))

    # TODO 1: write a loop that:
    #   - asks for an item name
    #   - if it's "done", break out of the loop
    #   - otherwise ask for a quantity (convert the input to an int!)
    #   - call cart.add_item(item_name, quantity)

    # TODO 2: ask "Loyalty member? (y/n): " and store True/False in
    # is_loyalty_member based on whether the answer starts with "y"

    # TODO 3: ask "Voucher code (or leave blank): " and store the result
    # in voucher_code — if the customer left it blank, use None instead
    # of an empty string

    # TODO 4: create a Checkout using cart, is_loyalty_member and
    # voucher_code, then generate and print the receipt

    # TODO 5: write the receipt string out to a file called "receipt.txt"
    # in this same folder, e.g.:
    #     with open("receipt.txt", "w") as f:
    #         f.write(receipt)


if __name__ == "__main__":
    main()
