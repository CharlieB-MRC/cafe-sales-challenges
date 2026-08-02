# 📦 03 — Stock Management

**Story:** The Trendiest's stockroom and fridge are a mess of half-counted ingredients. The manager needs a proper system to track how much of each item is left, warn the team when something's running low, and work out what to order from the supplier. Your job: build it, one challenge at a time.

Before starting, read the [main README](../README.md) if you haven't already — it explains forking, Codespaces, venv, and how to make a branch. Come back here once you're set up.

**Before you touch any file in this folder**, make sure you're on your own branch:
```bash
git checkout main
git pull
git checkout -b yourname-stock-management
```

---

## Challenges in this folder

| Tier | File | What you'll build | Learning focus |
|---|---|---|---|
| 🟢🟢 Very, very easy | [`tier1_very_easy/01_stock_summary.py`](tier1_very_easy/01_stock_summary.py) | Print a stockroom summary and total item count | `print()`, adding numbers |
| 🟢🟢 Very, very easy | [`tier1_very_easy/02_low_stock_check.py`](tier1_very_easy/02_low_stock_check.py) | Warn when one item's stock is below a threshold | single `if`/`else` |
| 🟢 Beginner | [`tier2_beginner/01_sell_stock.py`](tier2_beginner/01_sell_stock.py) | Reduce stock when an item is sold, without going below 0 | `input()`, dictionaries, `if`/`else` |
| 🟢 Beginner | [`tier2_beginner/02_reorder_list.py`](tier2_beginner/02_reorder_list.py) | Build a "needs reordering" list from the stock dictionary | loops, lists, dictionaries |
| 🟡 Intermediate | [`tier3_intermediate/01_stock_functions.py`](tier3_intermediate/01_stock_functions.py) | Rebuild stock logic using functions, with stock saved to a JSON file between runs | functions, `json.load`/`json.dump` |
| 🟡 Intermediate | [`tier3_intermediate/02_inventory_classes.py`](tier3_intermediate/02_inventory_classes.py) | Build `InventoryItem` and `Inventory` classes | classes, methods, `self` |
| 🔴 Challenging | [`tier4_challenging/inventory_system/`](tier4_challenging/inventory_system/) | A multi-file inventory system that loads/saves from CSV, raises low-stock alerts, and calculates supplier reorder amounts, with automated tests | multi-file projects, CSV files, `pytest` |
| 🔴 Challenging | [`tier4_challenging/stock_levels_visualisation/`](tier4_challenging/stock_levels_visualisation/) | Analyse a month of (pretend) daily stock readings and chart how items deplete and run out | `pandas`, `matplotlib`, data visualisation |

Work through the tiers in order if you're not sure where to start — each one builds on ideas from the last.

## Folder structure

```
03-stock-management/
├── README.md                          ← this file
├── tier1_very_easy/
│   ├── 01_stock_summary.py
│   └── 02_low_stock_check.py
├── tier2_beginner/
│   ├── 01_sell_stock.py
│   └── 02_reorder_list.py
├── tier3_intermediate/
│   ├── 01_stock_functions.py
│   └── 02_inventory_classes.py
└── tier4_challenging/
    ├── inventory_system/
    │   ├── inventory_data.csv
    │   ├── inventory.py
    │   ├── alerts.py
    │   ├── reorder.py
    │   ├── main.py
    │   └── test_inventory_system.py
    └── stock_levels_visualisation/
        ├── stock_levels.csv
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
   python tier1_very_easy/01_stock_summary.py
   ```
5. For the `tier4_challenging` folders, `cd` into that project's folder first, then run `main.py`:
   ```bash
   cd tier4_challenging/inventory_system
   python main.py
   ```
   And to run the automated tests:
   ```bash
   pytest
   ```
