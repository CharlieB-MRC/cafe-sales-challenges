# 🕹️ 05 — The Game Night Leaderboard

**Story:** The Trendiest runs a monthly retro arcade and board game tournament night for its regulars. Scores are flying in from the arcade cabinet, the trivia table, and the ping-pong corner — but the café's scoreboard system is a mess of scrap paper. Your job: build the leaderboard, the score tracker, and the tournament bracket, one challenge at a time.

Before starting, read the [main README](../README.md) if you haven't already — it explains forking, Codespaces, venv, and how to make a branch. Come back here once you're set up.

**Before you touch any file in this folder**, make sure you're on your own branch:
```bash
git checkout main
git pull
git checkout -b yourname-gaming-tournament
```

---

## Challenges in this folder

| Tier | File | What you'll build | Learning focus |
|---|---|---|---|
| 🟢🟢 Very, very easy | [`tier1_very_easy/01_print_leaderboard.py`](tier1_very_easy/01_print_leaderboard.py) | Print a 3-player leaderboard in a fixed order | `print()`, f-strings |
| 🟢🟢 Very, very easy | [`tier1_very_easy/02_who_won.py`](tier1_very_easy/02_who_won.py) | Work out who won a two-player round | `if`/`elif`/`else`, comparisons |
| 🟢 Beginner | [`tier2_beginner/01_sort_leaderboard.py`](tier2_beginner/01_sort_leaderboard.py) | Sort a list of scores into a ranked leaderboard | `sorted()`, `key=`, loops |
| 🟢 Beginner | [`tier2_beginner/02_score_tracker.py`](tier2_beginner/02_score_tracker.py) | Take scores live from players until they say "done" | `while` loops, `input()`, lists |
| 🟡 Intermediate | [`tier3_intermediate/01_tournament_functions.py`](tier3_intermediate/01_tournament_functions.py) | Rebuild score tracking using proper functions | functions, return values, code organisation |
| 🟡 Intermediate | [`tier3_intermediate/02_player_class.py`](tier3_intermediate/02_player_class.py) | Build a `Player` class that tracks scores across games | classes, methods, `self` |
| 🔴 Challenging | [`tier4_challenging/tournament_system/`](tier4_challenging/tournament_system/) | A multi-file single-elimination tournament bracket with a `Player` and `Tournament` class, results saved to CSV, and automated tests | multi-file projects, OOP, `pytest`, CSV files |
| 🔴 Challenging | [`tier4_challenging/tournament_visualisation/`](tier4_challenging/tournament_visualisation/) | Analyse several rounds of game night scores and chart player progression and total wins | `pandas`, `matplotlib`, data visualisation |

Work through the tiers in order if you're not sure where to start — each one builds on ideas from the last.

## Folder structure

```
05-gaming-tournament/
├── README.md                          ← this file
├── tier1_very_easy/
│   ├── 01_print_leaderboard.py
│   └── 02_who_won.py
├── tier2_beginner/
│   ├── 01_sort_leaderboard.py
│   └── 02_score_tracker.py
├── tier3_intermediate/
│   ├── 01_tournament_functions.py
│   └── 02_player_class.py
└── tier4_challenging/
    ├── tournament_system/
    │   ├── player.py
    │   ├── tournament.py
    │   ├── main.py
    │   └── test_tournament_system.py
    └── tournament_visualisation/
        ├── tournament_scores.csv
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
   python tier1_very_easy/01_print_leaderboard.py
   ```
5. For the `tier4_challenging` folders, `cd` into that project's folder first, then run `main.py`:
   ```bash
   cd tier4_challenging/tournament_system
   python main.py
   ```
   And to run the automated tests:
   ```bash
   pytest
   ```
