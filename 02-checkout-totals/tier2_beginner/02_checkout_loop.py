"""
CHALLENGE: Loop-Based Checkout Calculator
DIFFICULTY: Beginner
FOLDER: 02-checkout-totals / tier2_beginner

STORY
-----
It's rush hour and the till needs to scan items one by one. Keep asking
for prices until the customer says "done", then work out the subtotal,
the GST, and the final total they need to pay.

YOUR TASK
---------
1. Keep asking "Enter item price (or 'done' to finish): " in a loop.
2. If the customer types "done", stop asking.
3. Otherwise, convert what they typed to a float and add it to a running
   subtotal.
4. Once the loop ends, calculate GST as 10% of the subtotal, and the
   final total as subtotal + GST.
5. Print the subtotal, GST, and total, each rounded to 2 decimal places.

EXAMPLE OUTPUT
--------------
Enter item price (or 'done' to finish): 4.50
Enter item price (or 'done' to finish): 5.00
Enter item price (or 'done' to finish): done

Subtotal: $9.5
GST (10%): $0.95
Total: $10.45

HINTS
-----
- Use `while True:` and `break` when the user types "done".
- subtotal = 0 before the loop starts, then subtotal += float(entry)
  inside the loop.
- round(value, 2) keeps the money looking tidy.
"""

GST_RATE = 0.10

subtotal = 0

# TODO: write a while loop that:
#   - asks "Enter item price (or 'done' to finish): "
#   - if the answer is "done", stops the loop
#   - otherwise converts the answer to a float and adds it to subtotal


# TODO: after the loop, calculate gst_amount (subtotal * GST_RATE)
# and total (subtotal + gst_amount), then print all three values
# rounded to 2 decimal places, matching the EXAMPLE OUTPUT above.
