"""
CHALLENGE: Build a Customer Class
DIFFICULTY: Intermediate
FOLDER: 04-customer-info / tier3_intermediate

STORY
-----
The café wants each loyalty card member to be its own self-contained
"thing" in the code, with their own name, email, and points, plus the
ability to earn and redeem points safely — that's exactly what a class is
for.

YOUR TASK
---------
Complete the `Customer` class below by implementing each method
described in its docstring. Then test it using the code at the bottom of
the file.

EXAMPLE OUTPUT (from the test code at the bottom)
--------------------------------------------------
Priya Nair <priya@example.com> - 150 points
Priya Nair <priya@example.com> - 100 points
Sorry, Priya Nair only has 100 points, can't redeem 500.
Priya Nair <priya@example.com> - 100 points
"""


class Customer:
    """Represents one The Trendiest loyalty card member."""

    def __init__(self, name, email):
        """
        Set up a new customer with the given name and email, starting on
        0 points.

        Hint: store self.name, self.email, and self.points (starts at 0).
        """
        # TODO: implement this method
        pass

    def add_points(self, amount):
        """Add `amount` to self.points."""
        # TODO: implement this method
        pass

    def redeem_points(self, amount):
        """
        Subtract `amount` from self.points, but ONLY if the customer has
        enough points. If they don't have enough, print:
        "Sorry, {name} only has {points} points, can't redeem {amount}."
        and don't change self.points.
        """
        # TODO: implement this method
        pass

    def __str__(self):
        """
        Return a nice summary string in this exact format:
        "{name} <{email}> - {points} points"
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    customer = Customer("Priya Nair", "priya@example.com")
    customer.add_points(150)
    print(customer)

    customer.redeem_points(50)
    print(customer)

    customer.redeem_points(500)
    print(customer)
