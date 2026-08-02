"""
CHALLENGE: Build a SplitBill Class
DIFFICULTY: Intermediate
FOLDER: 02-checkout-totals / tier3_intermediate

STORY
-----
A group of friends has finished lunch at The Trendiest and wants to split
the bill evenly. This is trickier than it sounds — if you divide dollars
with plain division you can lose or gain fractions of a cent, and someone
ends up shortchanged. The trick is to work in CENTS (whole numbers)
internally, then hand any leftover cents out one at a time.

YOUR TASK
---------
Complete the `SplitBill` class below by implementing each method
described in its docstring. Then test it using the code at the bottom
of the file.

EXAMPLE OUTPUT (from the test code at the bottom)
--------------------------------------------------
Added $12.5 to the bill.
Added $9.0 to the bill.
Added $8.0 to the bill.
Total bill: $29.5
Split between 3 friends: [9.84, 9.83, 9.83]

HINTS
-----
- Multiply dollar amounts by 100 and round to get whole cents:
  round(price * 100) — this avoids floating point rounding weirdness.
- total_cents // n gives each person's even share in cents.
- total_cents % n gives the number of leftover cents to hand out one at
  a time (e.g. give the first `remainder` people 1 extra cent each).
"""


class SplitBill:
    """Holds a group bill at The Trendiest and splits it fairly."""

    def __init__(self):
        """Set up an empty bill. Hint: you'll need a list to store prices."""
        # TODO: create self.prices as an empty list
        pass

    def add_item(self, price):
        """
        Add `price` (a dollar amount, e.g. 12.50) to this bill.
        Print "Added ${price} to the bill."
        """
        # TODO: implement this method
        pass

    def get_total(self):
        """Return the total of everything in self.prices, in dollars."""
        # TODO: implement this method
        pass

    def split_between(self, n):
        """
        Split the total bill evenly between `n` friends, returning a
        list of `n` dollar amounts (floats, 2 decimal places) that add
        up EXACTLY to the total — no cent lost or gained anywhere.

        Steps:
          1. Convert the total to whole cents: total_cents = round(self.get_total() * 100)
          2. share_cents = total_cents // n   (everyone's even share)
          3. remainder = total_cents % n      (leftover cents to hand out)
          4. Build a list of n shares, each starting at share_cents.
          5. Add 1 extra cent to the first `remainder` people in the list
             (so the leftover cents aren't lost).
          6. Convert every share back to dollars (divide by 100, round
             to 2 decimal places) and return the list.
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    bill = SplitBill()
    bill.add_item(12.50)
    bill.add_item(9.00)
    bill.add_item(8.00)

    print(f"Total bill: ${bill.get_total()}")
    print(f"Split between 3 friends: {bill.split_between(3)}")
