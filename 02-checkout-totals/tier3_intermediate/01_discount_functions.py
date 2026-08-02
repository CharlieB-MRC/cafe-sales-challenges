"""
CHALLENGE: Build a Discount Engine With Functions
DIFFICULTY: Intermediate
FOLDER: 02-checkout-totals / tier3_intermediate

STORY
-----
The Trendiest is running promotions: some customers have a percentage-off
voucher, others have a flat-dollar-amount voucher, and everyone still
has to pay 10% GST. The head barista wants this logic written as clean,
reusable functions instead of one big tangled block of code.

YOUR TASK
---------
Implement the four functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom to work through a full checkout.

EXAMPLE OUTPUT
--------------
Subtotal: $50.0
After 20% discount: $40.0
After GST: $44.0

Subtotal: $50.0
After $5 flat discount: $45.0
After GST: $49.5
"""


def apply_percentage_discount(total, percent):
    """
    Return `total` reduced by `percent` percent.

    Example:
        apply_percentage_discount(50, 20) -> 40.0
        (50 reduced by 20% is 40)
    """
    # TODO: implement this function
    pass


def apply_flat_discount(total, amount):
    """
    Return `total` reduced by a flat dollar `amount`. The result should
    never go below 0 (a voucher can't make the bill negative!).

    Example:
        apply_flat_discount(50, 5) -> 45
        apply_flat_discount(3, 5) -> 0
    """
    # TODO: implement this function
    pass


def add_gst(total, gst_rate=0.10):
    """
    Return `total` with GST added on top, using gst_rate (default 10%).

    Example:
        add_gst(40) -> 44.0
    """
    # TODO: implement this function
    pass


def calculate_final_total(subtotal, percentage_discount=0, flat_discount=0):
    """
    Combine a subtotal with an OPTIONAL percentage discount, an OPTIONAL
    flat discount, and GST, in this order:
        1. Apply the percentage discount (if percentage_discount > 0).
        2. Apply the flat discount (if flat_discount > 0).
        3. Add GST.
    Return the final total, rounded to 2 decimal places.

    Example:
        calculate_final_total(50, percentage_discount=20) -> 44.0
        calculate_final_total(50, flat_discount=5) -> 49.5
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    subtotal = 50.0

    # TODO 1: call calculate_final_total with a 20% percentage discount
    # and print "Subtotal: $50.0", "After 20% discount: $40.0", and
    # "After GST: $44.0" (see EXAMPLE OUTPUT — you'll need
    # apply_percentage_discount and add_gst directly here to show each step)

    print()

    # TODO 2: do the same again but with a $5 flat discount instead,
    # printing "Subtotal: $50.0", "After $5 flat discount: $45.0", and
    # "After GST: $49.5"
