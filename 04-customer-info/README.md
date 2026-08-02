# 💳 04 — The Loyalty Card System

**Story:** The Trendiest's loyalty card scheme is taking off, but the customer records are a mess — some are scribbled on paper, some are trapped in an old spreadsheet, and none of it talks to the till. Your job: build the code that stores customer details, tracks their loyalty points, and finds the café's best customers.

Before starting, read the [main README](../README.md) if you haven't already — it explains forking, Codespaces, venv, and how to make a branch. Come back here once you're set up.

**Before you touch any file in this folder**, make sure you're on your own branch:
```bash
git checkout main
git pull
git checkout -b yourname-customer-info
```

---

## Challenges in this folder

| Tier | File | What you'll build | Learning focus |
|---|---|---|---|
| 🟢🟢 Very, very easy | [`tier1_very_easy/01_loyalty_card_summary.py`](tier1_very_easy/01_loyalty_card_summary.py) | Print a loyalty card summary line | `print()`, combining text and numbers |
| 🟢🟢 Very, very easy | [`tier1_very_easy/02_points_earned.py`](tier1_very_easy/02_points_earned.py) | Work out points earned from a spend amount | simple maths, `//` |
| 🟢 Beginner | [`tier2_beginner/01_lookup_customer.py`](tier2_beginner/01_lookup_customer.py) | Look up a customer by ID at the counter | `input()`, dictionaries, `if`/`else` |
| 🟢 Beginner | [`tier2_beginner/02_register_customers.py`](tier2_beginner/02_register_customers.py) | Register new customers signing up on launch day | `while` loops, lists of dictionaries |
| 🟡 Intermediate | [`tier3_intermediate/01_customer_functions.py`](tier3_intermediate/01_customer_functions.py) | Rebuild customer management using functions, saved to a JSON file | functions, return values, JSON files |
| 🟡 Intermediate | [`tier3_intermediate/02_customer_class.py`](tier3_intermediate/02_customer_class.py) | Build a `Customer` class that earns and redeems points | classes, methods, `self` |
| 🔴 Challenging | [`tier4_challenging/loyalty_system/`](tier4_challenging/loyalty_system/) | A multi-file loyalty system with `Customer` and `CustomerDatabase` classes, CSV records, membership tiers, and automated tests | multi-file projects, CSV files, `pytest` |
| 🔴 Challenging | [`tier4_challenging/customer_spend_visualisation/`](tier4_challenging/customer_spend_visualisation/) | Analyse 160 (pretend) loyalty customers and chart their spending habits | `pandas`, `matplotlib`, data visualisation |

Work through the tiers in order if you're not sure where to start — each one builds on ideas from the last.

## Folder structure

```
04-customer-info/
├── README.md                          ← this file
├── tier1_very_easy/
│   ├── 01_loyalty_card_summary.py
│   └── 02_points_earned.py
├── tier2_beginner/
│   ├── 01_lookup_customer.py
│   └── 02_register_customers.py
├── tier3_intermediate/
│   ├── 01_customer_functions.py
│   └── 02_customer_class.py
└── tier4_challenging/
    ├── loyalty_system/
    │   ├── customers_data.csv
    │   ├── customer.py
    │   ├── database.py
    │   ├── main.py
    │   └── test_loyalty_system.py
    └── customer_spend_visualisation/
        ├── customer_spend.csv
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
   python tier1_very_easy/01_loyalty_card_summary.py
   ```
5. For the `tier4_challenging` folders, `cd` into that project's folder first, then run `main.py`:
   ```bash
   cd tier4_challenging/loyalty_system
   python main.py
   ```
   And to run the automated tests:
   ```bash
   pytest
   ```
