"""
Task 2: Guess the Number Game
Features:
- Random integer generation within a customizable range.
- Real-time hints (Higher/Lower) for user guesses.
- Attempt counter and score tracking.
- Robust input validation to prevent crashes from non-numeric input.
"""

import random


class GuessNumberGame:
    def __init__(self, lower_bound: int = 1, upper_bound: int = 100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.target_number = 0
        self.attempts = 0
        self.is_active = False

    def start_new_game(self):
        self.target_number = random.randint(self.lower_bound, self.upper_bound)
        self.attempts = 0
        self.is_active = True

    def evaluate_guess(self, guess: int) -> str:
        """
        Compares the guess with the target number.
        Returns: 'LOW', 'HIGH', 'CORRECT', or 'OUT_OF_BOUNDS'
        """
        if guess < self.lower_bound or guess > self.upper_bound:
            return "OUT_OF_BOUNDS"
        
        self.attempts += 1
        if guess < self.target_number:
            return "LOW"
        elif guess > self.target_number:
            return "HIGH"
        else:
            self.is_active = False
            return "CORRECT"

    def play(self):
        self.start_new_game()
        print("\n==========================================")
        print("        GUESS THE NUMBER GAME             ")
        print("==========================================")
        print(f"I have selected a number between {self.lower_bound} and {self.upper_bound}.")
        print("Can you guess what it is?")

        while self.is_active:
            raw_input = input(f"\nEnter your guess ({self.lower_bound}-{self.upper_bound}): ").strip()
            
            try:
                guess = int(raw_input)
            except ValueError:
                print("Invalid input! Please enter a valid whole number.")
                continue

            result = self.evaluate_guess(guess)

            if result == "OUT_OF_BOUNDS":
                print(f"Out of range! Please enter a number between {self.lower_bound} and {self.upper_bound}.")
            elif result == "LOW":
                print("Too Low! Try a higher number.")
            elif result == "HIGH":
                print("Too High! Try a lower number.")
            elif result == "CORRECT":
                print(f"\nCongratulations! You found the number {self.target_number} in {self.attempts} attempts.")
                break


def main():
    while True:
        game = GuessNumberGame(1, 100)
        game.play()
        
        play_again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if play_again not in ("y", "yes"):
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()