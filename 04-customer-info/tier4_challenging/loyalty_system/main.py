"""
CHALLENGE PART 3 of 3: Putting It All Together

Complete customer.py and database.py first. This file ties them all
together into a program you can actually run.

YOUR TASK
---------
Write a program that:
  1. Loads the CustomerDatabase from customers_data.csv.
  2. Prints every customer and their current tier.
  3. Prints the top 3 customers by points.
  4. Registers a brand new customer ("Nadia Kim", "nadia@example.com"),
     adds them 120 points, and prints their summary.
  5. Saves the database back to customers_data.csv.

Run it with:
    python main.py
"""

from database import CustomerDatabase


def main():
    db = CustomerDatabase()

    print("All customers:")
    # TODO 1: loop over db.customers and print each one (print(customer)
    # will use the __str__ method you wrote in customer.py)

    print("\nTop 3 customers:")
    # TODO 2: get the top 3 customers using db.top_customers(3) and print
    # each one

    print("\nRegistering a new customer:")
    # TODO 3: register "Nadia Kim" with email "nadia@example.com" using
    # db.register_customer(...), then call add_points(120) on the
    # Customer object that was returned, then print it

    # TODO 4: save the database back to its CSV file using db.save()
    print("\nSaved database.")


if __name__ == "__main__":
    main()
