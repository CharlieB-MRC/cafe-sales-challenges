# 🧾 01 — The Point-of-Sale (POS) System

**Story:** The Trendiest's ordering screen at the counter has gone blank. Baristas need a working system to look up menu items, take orders, and print receipts. Your job: rebuild it, one challenge at a time.

Before starting, read the [main README](../README.md) if you haven't already — it explains forking, Codespaces, venv, and how to make a branch. Come back here once you're set up.

**Before you touch any file in this folder**, make sure you're on your own branch:
```bash
git checkout main
git pull
git checkout -b yourname-cafe-pos
```

---

## Challenges in this folder

| Tier | File | What you'll build | Learning focus |
|---|---|---|---|
| 🟢🟢 Very, very easy | [`tier1_very_easy/01_print_menu.py`](tier1_very_easy/01_print_menu.py) | Print the café's menu board | `print()`, plain text output |
| 🟢🟢 Very, very easy | [`tier1_very_easy/02_order_confirmation.py`](tier1_very_easy/02_order_confirmation.py) | Print a one-line order confirmation | f-strings, combining text and numbers |
| 🟢 Beginner | [`tier2_beginner/01_order_one_item.py`](tier2_beginner/01_order_one_item.py) | Look up the price of one item a customer asks for | `input()`, dictionaries, `if`/`else` |
| 🟢 Beginner | [`tier2_beginner/02_order_multiple_items.py`](tier2_beginner/02_order_multiple_items.py) | Take a whole order, item by item, until the customer is done | `while` loops, running totals |
| 🟡 Intermediate | [`tier3_intermediate/01_menu_functions.py`](tier3_intermediate/01_menu_functions.py) | Rebuild the ordering logic using proper functions | functions, return values, code organisation |
| 🟡 Intermediate | [`tier3_intermediate/02_order_class.py`](tier3_intermediate/02_order_class.py) | Build an `Order` class that holds and manages a customer's order | classes, methods, `self` |
| 🔴 Challenging | [`tier4_challenging/pos_system/`](tier4_challenging/pos_system/) | A multi-file mini POS application with a menu loaded from a data file, an `Order` class, receipt generation (with GST), and automated tests | multi-file projects, JSON files, `pytest` |
| 🔴 Challenging | [`tier4_challenging/sales_trends_visualisation/`](tier4_challenging/sales_trends_visualisation/) | Analyse a week of (pretend) POS sales data and chart the café's best sellers | `pandas`, `matplotlib`, data visualisation |

Work through the tiers in order if you're not sure where to start — each one builds on ideas from the last.

## Folder structure

```
01-cafe-pos/
├── README.md                          ← this file
├── tier1_very_easy/
│   ├── 01_print_menu.py
│   └── 02_order_confirmation.py
├── tier2_beginner/
│   ├── 01_order_one_item.py
│   └── 02_order_multiple_items.py
├── tier3_intermediate/
│   ├── 01_menu_functions.py
│   └── 02_order_class.py
└── tier4_challenging/
    ├── pos_system/
    │   ├── menu_data.json
    │   ├── menu.py
    │   ├── order.py
    │   ├── receipt.py
    │   ├── main.py
    │   └── test_pos_system.py
    └── sales_trends_visualisation/
        ├── weekly_sales.csv
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
   python tier1_very_easy/01_print_menu.py
   ```
5. For the `tier4_challenging` folders, `cd` into that project's folder first, then run `main.py`:
   ```bash
   cd tier4_challenging/pos_system
   python main.py
   ```
   And to run the automated tests:
   ```bash
   pytest
   ```
