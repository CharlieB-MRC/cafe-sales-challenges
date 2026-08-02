"""
CHALLENGE: Add 10% GST to a Price
DIFFICULTY: Very, very easy
FOLDER: 02-checkout-totals / tier1_very_easy

STORY
-----
The Trendiest has to add 10% GST (Australia's Goods and Services Tax) onto
every sale before it hits the till. A customer is buying one Toastie —
your job is to work out what they actually pay, GST included.

YOUR TASK
---------
The price and the GST rate are already stored in variables below. Find
the line marked "# TODO" and write ONE line of code that works out the
price including GST, then run the file and check your output matches
the EXAMPLE OUTPUT exactly.

EXAMPLE OUTPUT
--------------
Price (before GST): $6.5
GST (10%): $0.65
Price (including GST): $7.15

HINT
----
- GST amount = price * gst_rate
- price including GST = price + GST amount
  (or in one step: price * (1 + gst_rate))
"""

price = 6.50
gst_rate = 0.10

gst_amount = price * gst_rate

# TODO: calculate the price including GST (price + gst_amount)
# and store it in a variable called price_with_gst
price_with_gst = None

print(f"Price (before GST): ${price}")
print(f"GST (10%): ${round(gst_amount, 2)}")
print(f"Price (including GST): ${price_with_gst}")
