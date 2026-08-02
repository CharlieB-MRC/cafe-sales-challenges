"""
CHALLENGE PART 2 of 3: The Customer Database

See customer.py for an overview of this whole project. Complete
customer.py first, since this file needs it.

YOUR TASK (this file)
----------------------
Build a CustomerDatabase class that loads customer records from a CSV
file into a list of Customer objects, can find/register/update
customers, and can save everything back to a CSV file.

customers_data.csv has these columns:
    name, email, points
"""

import csv

from customer import Customer


class CustomerDatabase:
    """Holds and manages every The Trendiest loyalty card member."""

    def __init__(self, csv_path="customers_data.csv"):
        """
        Store csv_path, then load all customers from it into
        self.customers, a list of Customer objects.

        Hint:
            with open(csv_path, newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    ...

            Remember row["points"] will be a string — convert it to int!
        """
        # TODO: implement this method
        pass

    def find_customer(self, email):
        """
        Return the Customer object in self.customers whose email matches
        `email`, or None if no customer has that email.
        """
        # TODO: implement this method
        pass

    def register_customer(self, name, email):
        """
        Create a new Customer (0 points) with the given name and email,
        add it to self.customers, and return it.
        If a customer with that email already exists, don't add a
        duplicate — just return the existing one instead.
        """
        # TODO: implement this method
        pass

    def top_customers(self, count=3):
        """
        Return a list of the `count` customers with the most points,
        sorted from highest to lowest points.
        """
        # TODO: implement this method
        pass

    def save(self, csv_path=None):
        """
        Write every customer in self.customers back out to a CSV file
        with columns name, email, points. If csv_path is None, use
        self.csv_path (the path this database was loaded from).

        Hint:
            with open(path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "email", "points"])
                for c in self.customers:
                    writer.writerow([c.name, c.email, c.points])
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    db = CustomerDatabase()
    print(f"Loaded {len(db.customers)} customers.")
    for customer in db.top_customers(3):
        print(customer)
