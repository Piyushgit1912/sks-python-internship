# Task 2: Guess the Number Game

**Intern Name:** Piyush Upadhyay  
**Reference ID:** SKS/A2/C149158  
**Domain:** Python Development  
**Organization:** Saiket Systems  

---

## Overview

Task 2 focuses on creating an interactive, command-line number guessing game in Python. The program generates a random integer within a specified range (1 to 100) and guides the player with dynamic feedback ("Too Low" / "Too High") while recording the total number of attempts until a correct guess is made.

---

## Technical Details

* **Random Selection:** Leverages Python's `random.randint()` to generate a target number within specified boundaries.
* **OOP Design:** Encapsulated within the `GuessNumberGame` class to manage game boundaries, target values, active status, and attempt tracking.
* **Modular Evaluation:** The `evaluate_guess()` method compares values and returns distinct states (`LOW`, `HIGH`, `CORRECT`, `OUT_OF_BOUNDS`) to separate business logic from user interface prints.
* **Input Validation & Safety:** Implements `try-except (ValueError)` handling to safely manage invalid/non-numeric inputs and ensures boundary violations do not count against the user's valid attempts.

---

## Project Structure

```text
Task_2_Guess_Number/
├── guess_game.py       # Main Python source code
├── test_guess_game.py  # Pytest unit tests
└── README.md           # Documentation & test report

