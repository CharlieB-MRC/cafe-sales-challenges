# ☕ The Trendiest Café, Coding Challenges

Welcome to **The Trendiest** café, they need YOUR help. The café's old computer systems broke down, and it's your job to write the code that fixes them. Everything from the till at the counter, to tracking the milk in the fridge, right through to the scoreboard for café game night.

This repository is full of coding challenges based on one big shared theme: **the café**. There's something here for everyone, from your very first lines of Python, all the way up to proper data science with charts and graphs. Nobody is expected to do everything. Pick a folder, pick a difficulty, and start coding.

This README explains **everything you need to know** to get set up, including things you may never have done before (forking, branching, virtual environments). Go slowly, follow the steps in order, and don't skip ahead, every step matters.

Note: 

---

## 🗺️ What's inside this repository

| # | Folder | Café system | What you'll practise |
|---|--------|-------------|------------------------|
| 1 | [`01-cafe-pos/`](01-cafe-pos/) | The Point-of-Sale (ordering) system | variables, `if`/`else`, dictionaries, functions, classes, mini data visualisation |
| 2 | [`02-checkout-totals/`](02-checkout-totals/) | The checkout & till | maths, discounts, tax, splitting bills, receipts |
| 3 | [`03-stock-management/`](03-stock-management/) | The stockroom / fridge | tracking numbers, loops, files, low-stock alerts |
| 4 | [`04-customer-info/`](04-customer-info/) | The loyalty card system | storing records, searching data, customer classes |
| 5 | [`05-gaming-tournament/`](05-gaming-tournament/) | Café game night leaderboard | sorting, ranking, tournaments, classes, charts |

Each folder has its **own README.md** with the full list of challenges for that system. Open a folder above to see what's inside it. Or see [CHALLENGE_MAP.md](CHALLENGE_MAP.md) for all 40 challenges on one page.

---

## 🚦 Difficulty levels

Every challenge lives inside a tier folder, so you always know how hard it is before you open it:

| Tier folder | Difficulty | What it looks like |
|---|---|---|
| `tier1_very_easy` | 🟢🟢 **Very, very easy** | One small Python file. Mostly `print()`, variables, and simple maths. Great for your very first challenge ever. |
| `tier2_beginner` | 🟢 **Beginner** | One Python file. Uses `input()`, `if`/`else`, loops, and lists or dictionaries. |
| `tier3_intermediate` | 🟡 **Intermediate** | One Python file, but organised into **functions** and sometimes a simple **class**. You'll need to plan before you code. |
| `tier4_challenging` | 🔴 **Challenging** | A small **project made of several files** (classes, tests, and sometimes real data). Includes data visualisation / mini data-science challenges using `pandas` and `matplotlib`. Appropriately tough for Year 10, take your time. |

You do not have to go in order, but it's a good idea to start at `tier1_very_easy` in a folder before jumping to the harder tiers of the *same* folder, since later challenges often build on earlier ideas.

---

## 🧭 Overview: the whole process, in one glance
*Each step is explained further below this section.*

1. **Fork** this repository (make your own copy of it on GitHub).
2. Open your fork in **GitHub Codespaces** (easiest, no installing anything) **or** clone it to your own computer.
3. Set up a **virtual environment (venv)** and install `requirements.txt`.
4. Create a **new branch** for the folder/challenge you're about to work on.
5. Open a challenge file, read the instructions at the top, and write your code.
6. **Commit** and **push** your work often.
7. Repeat steps 4–6 for every new folder you tackle (a new branch each time).

Now let's go through every one of these steps slowly, in detail.

---

## Step 1, Fork this repository

"Forking" means making your **own personal copy** of this repository, under your own GitHub account, so you can make changes without affecting anyone else's work.

1. Make sure you're logged into GitHub.
2. Go to the top of this repository's page on GitHub.
3. Click the **Fork** button in the top-right corner.
4. Leave the settings as they are and click **Create fork**.
5. GitHub will take you to *your own copy* of the repository. Check the top-left, it should now say `your-username/cafe-sales-challenges`.

You'll do all your work in **your fork**, not the original repository. That's totally normal and expected.

---

## Step 2, Open the code (choose ONE option)

### Option A (recommended): GitHub Codespaces, nothing to install

Codespaces gives you a full coding computer that runs in your web browser. It already has Python installed, so it's the fastest way to get started.

1. On **your fork's** GitHub page, click the green **`<> Code`** button.
2. Click the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Wait about 30–60 seconds while it builds your environment, you'll see a loading screen.
5. A code editor (it looks like VS Code) will open right in your browser, already connected to your forked repository. You're in!

You can open a Terminal inside Codespaces by going to the menu: **Terminal → New Terminal**. You'll use this terminal for every command below.

To come back to the same codespace later, go to your fork on GitHub → **Code** → **Codespaces** tab → click on the codespace you already made (don't create a new one each time).

### Option B: Work on your own computer

Only do this if your teacher has told you to, or Codespaces isn't available.

1. Install [Git](https://git-scm.com/downloads) and [Python 3.11+](https://www.python.org/downloads/) if you don't already have them.
2. On **your fork's** GitHub page, click the green **`<> Code`** button and copy the HTTPS link (it looks like `https://github.com/your-username/cafe-sales-challenges.git`).
3. Open a terminal (Command Prompt, PowerShell, or Terminal app) and run:
   ```bash
   git clone https://github.com/your-username/cafe-sales-challenges.git
   cd cafe-sales-challenges
   ```
4. You now have the code on your computer, inside a folder called `cafe-sales-challenges`.

---

## Step 3, Set up your virtual environment (venv)

A **virtual environment** is a private, clean toolbox of Python packages just for this project, so it doesn't get mixed up with anything else on your computer (or Codespace). You only need to **create** it once, but you'll **activate** it every time you sit down to work.

Make sure your terminal is inside the `cafe-sales-challenges` folder before running these.

### Create the venv (do this once)

**Mac / Linux / Codespaces terminal:**
```bash
python3 -m venv venv
```

**Windows (Command Prompt or PowerShell):**
```bash
python -m venv venv
```

This creates a new folder called `venv/` inside your project. That folder holds your own private copy of Python, you can ignore its contents, you'll never open it directly.

### Activate the venv (do this every time you start working)

**Mac / Linux / Codespaces terminal:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

✅ **How do I know it worked?** Your terminal prompt will now start with `(venv)`, like this:
```
(venv) your-name@computer cafe-sales-challenges %
```
If you don't see `(venv)` at the start of the line, it isn't active, run the activate command again.

When you're finished working for the day, you can type `deactivate` to switch it off (optional, closing the terminal also does this).

### Install the required packages

With your venv **activated**, run:
```bash
pip install -r requirements.txt
```

This reads the [`requirements.txt`](requirements.txt) file in this repository and installs every package listed inside it (things like `pandas` for handling data, and `matplotlib` for drawing charts). You only need to run this once per venv, but if you ever pull down new code that added something new to `requirements.txt`, run it again to stay up to date.

---

## Step 4, Create your own branch

A **branch** is like a separate timeline for your code, a safe space to make changes without touching the `main` timeline. You should **make a new branch every time you start a new challenge folder.**

Name your branches like this: `yourname-foldername`, for example:

```bash
git checkout -b steve-cafe-pos
```

This does two things at once: it **creates** a new branch called `steve-cafe-pos`, and it **switches** you onto it. Use your own first name and the folder you're about to work in (`cafe-pos`, `checkout-totals`, `stock-management`, `customer-info`, or `gaming-tournament`).

You can check which branch you're currently on at any time with:
```bash
git branch
```
The branch you're on will have a little `*` next to it.

**Remember:** when you move to a *different* challenge folder later, switch back to `main` first, then make a *new* branch for that folder:
```bash
git checkout main
git checkout -b steve-checkout-totals
```

---

## Step 5, Pick a challenge and write your code

1. Open one of the 5 folders (see the table near the top of this README).
2. Read that folder's own `README.md`, it lists every challenge available, in order of difficulty.
3. Open a challenge file (e.g. `01_print_menu.py`). Every challenge file starts with a comment block explaining:
   - **What the challenge is asking you to do**
   - **What your output should look like**
   - Any `# TODO:` comments marking exactly where to write your code
4. Write your code where the `TODO` comments are. Don't delete the comments, they help you (and your teacher) understand what each part does.
5. Run your file to test it. In the terminal:
   ```bash
   python filename.py
   ```
   (On some setups you may need `python3` instead of `python`.)
6. Compare your output to the example in the comment block. Keep editing and re-running until it matches.
7. Some `tier4_challenging` folders include a **tests file** (starts with `test_`). Run it with:
   ```bash
   pytest
   ```
   This will automatically check your code and tell you what's passing ✅ and what still needs work ❌.

---

## Step 6, Save your work with Git (add, commit, push)

Do this **often**, every time you finish a challenge, or even a small chunk of one. Never wait until the very end!

1. **Check what's changed:**
   ```bash
   git status
   ```
   This shows which files you've edited, in red.

2. **Stage your changes** (tell Git which files to save):
   ```bash
   git add .
   ```
   The `.` means "everything I've changed."

3. **Commit your changes** (save a snapshot, with a short note about what you did):
   ```bash
   git commit -m "Finished the print menu challenge"
   ```
   Write a real, honest message describing what you actually did, future-you will thank you.

4. **Push your changes** (upload your commit to your fork on GitHub):
   ```bash
   git push origin steve-cafe-pos
   ```
   (Replace `steve-cafe-pos` with whatever your branch is actually called.)

The **very first time** you push a brand-new branch, Git might show you a suggested command with `--set-upstream`, that's fine, you can copy and run exactly what it suggests.

---

## Step 7, Repeat for the next folder

Every time you start a new challenge folder:

```bash
git checkout main        # go back to the clean starting point
git pull                 # make sure main is up to date
git checkout -b yourname-foldername   # make a fresh branch
```

Then repeat Steps 5 and 6 inside that folder.

---

## Step 8 (optional), Submitting your work

Your teacher will tell you whether they want you to:
- **Open a Pull Request**, on GitHub, go to your fork, click **Pull requests → New pull request**, and follow the prompts to compare your branch against `main`. This is how you'd propose your changes be added back, your teacher can view and comment on your code this way.
- Or simply **share the link to your fork** and your branches, so your teacher can look at your code directly.

Either way, make sure everything is **pushed** (Step 6) before you consider a challenge "done."

---

## 🆘 Troubleshooting / FAQ

**"command not found: python" or "python is not recognised"**
Try `python3` instead of `python`. If neither works, Python may not be installed, ask your teacher, or use Codespaces instead (it's already installed there).

**I forgot to activate my venv and now `pip install` isn't working / packages are "missing"**
Go back to Step 3 and run the *activate* command again. Check for `(venv)` at the start of your terminal line before installing or running anything.

**"Permission denied" when running an activate script on Windows**
In PowerShell, run this once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then try activating again.

**I think I broke my file and want to undo everything since my last commit**
```bash
git checkout -- filename.py
```
This throws away *uncommitted* changes to that file and restores your last saved commit. Be careful, this cannot be undone.

**Git says I have a "merge conflict"**
This means Git found two different versions of the same lines and isn't sure which to keep. Don't panic, ask your teacher to walk through it with you the first time you see this.

**My code runs but gives the wrong answer**
Read the error or the output carefully, Python's error messages usually tell you exactly which line and what went wrong. Add extra `print()` statements to see what your variables actually contain at each step.

---

## 💡 Tips for success

- Run your code **often**, after every few lines, not just at the end.
- Read error messages properly. They look scary but are usually very specific and helpful.
- It's completely normal to get stuck. Getting stuck is part of coding, ask a classmate or your teacher.
- Commit small, commit often. Little commits with clear messages are much easier to fix than one giant commit at the end.
- Don't just copy an answer from the internet without understanding it, you'll need these skills again in the next challenge!

---

## 📁 Repository structure

```
cafe-sales-challenges/
├── README.md                  ← you are here
├── requirements.txt           ← list of Python packages to install
├── .gitignore
├── 01-cafe-pos/
│   ├── README.md
│   ├── tier1_very_easy/
│   ├── tier2_beginner/
│   ├── tier3_intermediate/
│   └── tier4_challenging/
├── 02-checkout-totals/        (same structure)
├── 03-stock-management/       (same structure)
├── 04-customer-info/          (same structure)
└── 05-gaming-tournament/      (same structure)
```

Good luck, and welcome to the The Trendiest team. ☕💻
