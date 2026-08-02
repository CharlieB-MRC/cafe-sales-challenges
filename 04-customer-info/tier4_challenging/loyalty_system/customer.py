"""
CHALLENGE PART 1 of 3: The Customer

This project (loyalty_system) is split across several files that work
together:
    customers_data.csv - the raw customer records (already provided)
    customer.py         - (this file) a single loyalty card member
    database.py         - loads/saves/manages all customers
    main.py              - runs the whole program
    test_loyalty_system.py - automated checks for your code

Work through them in that order. Run `pytest` at any point to see which
parts are passing.

YOUR TASK (this file)
----------------------
Complete the Customer class so it stores a member's details and can work
out their current membership tier from their points.

Membership tiers:
    Bronze  - under 100 points
    Silver  - 100 to 299 points (inclusive)
    Gold    - 300 points or more
"""


class Customer:
    """Represents one The Trendiest loyalty card member."""

    def __init__(self, name, email, points=0):
        """
        Store name, email, and points (as an int) on this customer.
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
        enough points. Return True if the redemption succeeded, or False
        if they didn't have enough points (and don't change self.points
        in that case).
        """
        # TODO: implement this method
        pass

    def get_tier(self):
        """
        Return this customer's current membership tier as a string,
        based on self.points:
            "Bronze" if points < 100
            "Silver" if 100 <= points < 300
            "Gold"   if points >= 300
        """
        # TODO: implement this method
        pass

    def __str__(self):
        """
        Return a summary string in this exact format:
        "{name} <{email}> - {points} points ({tier})"
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    # Quick manual check while you're building this file.
    c = Customer("Priya Nair", "priya@example.com", 45)
    print(c)
    c.add_points(60)
    print(c)
    print("Tier now:", c.get_tier())
