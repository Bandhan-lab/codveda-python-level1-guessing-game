"""Codveda Level 1 - Task 2: Number Guessing Game.

The game generates a random number from 1 to 100 and gives the player
multiple attempts to guess it.
"""

import random
from typing import Optional


DEFAULT_MAX_ATTEMPTS = 10
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_target() -> int:
    """Return a random target number between 1 and 100."""
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_guess(prompt: str = "Enter your guess: ") -> Optional[int]:
    """Read and validate an integer guess.

    Returns None for invalid input so the caller can ask again.
    """
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return None


def check_guess(guess: int, target: int) -> str:
    """Compare a guess with the target and return feedback."""
    if guess < target:
        return "Too low!"
    if guess > target:
        return "Too high!"
    return "Correct!"


def play_game(
    target: Optional[int] = None,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
) -> bool:
    """Play one guessing game.

    Returns True when the player guesses correctly and False otherwise.
    """
    if target is None:
        target = generate_target()

    attempts = 0

    while attempts < max_attempts:
        guess = get_guess()

        if guess is None:
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            continue

        attempts += 1
        feedback = check_guess(guess, target)
        print(feedback)

        if feedback == "Correct!":
            print(f"You guessed the number in {attempts} attempt(s).")
            return True

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    print(f"Game over! The correct number was {target}.")
    return False


def main() -> None:
    """Run the interactive number guessing game."""
    print("=" * 34)
    print("       NUMBER GUESSING GAME")
    print("=" * 34)
    print(f"I'm thinking of a number from {MIN_NUMBER} to {MAX_NUMBER}.")
    print(f"You have {DEFAULT_MAX_ATTEMPTS} valid attempts to guess it.\\n")

    while True:
        play_game()

        replay = input("\\nPlay again? (y/n): ").strip().lower()
        if replay != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
