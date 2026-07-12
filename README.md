# Wordle Solver

A tool designed to analyze word lists and help you find the optimal words for solving Wordle puzzles.
The script uses Playwright and opens the official New York Times Wordle game in a browser window and solves the daily puzzle automatically.

## Features

### 1. Two Word Lists
* **`wordleans.txt`**: List of possible Wordle answers
* **`wordleans_all.txt`**: List of all valid guessable words

### 2. Three Solver Modes
* **Alphabetical Mode**: Picks the first available word from the list in alphabetical order.
* **Greedy Mode**: Counts the letter frequencies and calculates scores based on how common the unique letters are to maximize elimination.
* **Shannon Entropy Mode**: Calculates the information theory entropy for every word and picks the word with the highest entropy. This is the default mode.

---

## Getting Started

Make sure you have Python and the Playwright framework installed:

```bash
pip install playwright
playwright install
```

To run the automated solver, simply execute:

```bash
python main.py
```
