# 🧾 02 — Checkout Totals

**Story:** It's crunch time at the The Trendiest till. Customers are queuing up with cash, vouchers, and friends who want to split the bill — and every sale needs 10% GST added on top. Your job: rebuild the checkout maths, one challenge at a time.

Before starting, read the [main README](../README.md) if you haven't already — it explains forking, Codespaces, venv, and how to make a branch. Come back here once you're set up.

**Before you touch any file in this folder**, make sure you're on your own branch:
```bash
git checkout main
git pull
git checkout -b yourname-checkout-totals
```

---

## Challenges in this folder

| Tier | File | What you'll build | Learning focus |
|---|---|---|---|
| 🟢🟢 Very, very easy | [`tier1_very_easy/01_add_up_prices.py`](tier1_very_easy/01_add_up_prices.py) | Add up three prices on the counter | `print()`, simple maths |
| 🟢🟢 Very, very easy | [`tier1_very_easy/02_add_gst.py`](tier1_very_easy/02_add_gst.py) | Work out a price including 10% GST | one formula, `print()` |
| 🟢 Beginner | [`tier2_beginner/01_calculate_change.py`](tier2_beginner/01_calculate_change.py) | Work out a customer's change at the till | `input()`, `if`/`else` |
| 🟢 Beginner | [`tier2_beginner/02_checkout_loop.py`](tier2_beginner/02_checkout_loop.py) | Scan items one by one and total the bill with GST | `while` loops, running totals |
| 🟡 Intermediate | [`tier3_intermediate/01_discount_functions.py`](tier3_intermediate/01_discount_functions.py) | Build a reusable discount + GST engine | functions, return values |
| 🟡 Intermediate | [`tier3_intermediate/02_split_bill_class.py`](tier3_intermediate/02_split_bill_class.py) | Build a `SplitBill` class that divides a bill fairly, down to the cent | classes, methods, integer cents |
| 🔴 Challenging | [`tier4_challenging/receipt_system/`](tier4_challenging/receipt_system/) | A multi-file mini checkout application with a `Cart`, loyalty + voucher discounts, GST, receipt generation (printed and saved to a file), and automated tests | multi-file projects, JSON files, `pytest` |
| 🔴 Challenging | [`tier4_challenging/daily_totals_visualisation/`](tier4_challenging/daily_totals_visualisation/) | Analyse months of (pretend) daily checkout totals and chart revenue trends | `pandas`, `matplotlib`, data visualisation |

Work through the tiers in order if you're not sure where to start — each one builds on ideas from the last.

## Folder structure

```
02-checkout-totals/
├── README.md                          ← this file
├── tier1_very_easy/
│   ├── 01_add_up_prices.py
│   └── 02_add_gst.py
├── tier2_beginner/
│   ├── 01_calculate_change.py
│   └── 02_checkout_loop.py
├── tier3_intermediate/
│   ├── 01_discount_functions.py
│   └── 02_split_bill_class.py
└── tier4_challenging/
    ├── receipt_system/
    │   ├── menu_data.json
    │   ├── cart.py
    │   ├── checkout.py
    │   ├── main.py
    │   └── test_receipt_system.py
    └── daily_totals_visualisation/
        ├── daily_totals.csv
        ├── data_loader.py
        ├── visualise.py
        └── main.py
```

## How to run a challenge

1. Open the file in your editor.
2. Read the big comment block at the top — it explains the task and shows example output.
3. Fill in the parts marked `# TODO`.
4. Run it from your terminal (make sure your venv is active — see the main README):
   ```bash
   python tier1_very_easy/01_add_up_prices.py
   ```
5. For the `tier4_challenging` folders, `cd` into that project's folder first, then run `main.py`:
   ```bash
   cd tier4_challenging/receipt_system
   python main.py
   ```
   And to run the automated tests:
   ```bash
   pytest
   ```
