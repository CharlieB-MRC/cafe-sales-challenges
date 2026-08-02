"""
CHALLENGE PART 4 of 4: Putting It All Together

Complete inventory.py, alerts.py, and reorder.py first. This file ties
them all together into a program you can actually run and use like a real
stockroom management tool.

YOUR TASK
---------
Write a loop that:
  1. Creates an Inventory.
  2. Repeatedly asks the staff member what item (and how many) was sold,
     until they type "done".
  3. Once done, prints all low-stock alerts, then prints the supplier
     reorder summary, then saves the inventory back to CSV.

Run it with:
    python main.py
"""

from inventory import Inventory
from alerts import build_alert_messages
from reorder import print_reorder_summary


def main():
    inv = Inventory()

    print(
        "The Trendiest Stockroom — type an item name to record a sale, or 'done' to finish."
    )
    print("Tracked items:", ", ".join(inv.list_items()))

    # TODO: write a loop that:
    #   - asks for an item name
    #   - if it's "done", break out of the loop
    #   - otherwise ask for a quantity sold (convert the input to an int!)
    #   - call inv.sell(item_name, quantity)

    print()
    alerts = build_alert_messages(inv)
    if alerts:
        for message in alerts:
            print(message)
    else:
        print("No low stock alerts — everything looks fine.")

    print()
    print_reorder_summary(inv)

    inv.save()
    print("\nInventory saved back to inventory_data.csv.")


if __name__ == "__main__":
    main()
