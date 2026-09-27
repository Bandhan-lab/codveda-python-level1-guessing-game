# Number Guessing Game

A command-line Number Guessing Game built in Python for the Codveda Technology Python Development Internship — Level 1, Task 2.

## Features

- Generates a random number between 1 and 100.
- Allows multiple valid attempts.
- Gives "Too high!" or "Too low!" feedback.
- Detects a correct guess and reports the number of attempts.
- Ends the game after the maximum number of valid attempts.
- Handles non-numeric input and guesses outside the 1–100 range.
- Allows the player to start another round.

## Requirements

- Python 3.8 or newer

No external Python packages are required.

## Project Structure

```
codveda-python-level1-guessing-game/
├── guessing_game.py
├── tests/
│   └── test_guessing_game.py
├── README.md
└── .gitignore
```

## How to Run

Clone the repository and open it in VS Code or a terminal.

Run:

```bash
python3 guessing_game.py
```

Follow the prompts to enter guesses.

## How to Run Tests

Run the test suite from the project root:

```bash
python3 -m unittest discover -s tests -v
```

## Internship

Developed as part of the Python Development Internship at Codveda Technology.

Task: Level 1 — Task 2: Number Guessing Game

## Author

Bandhan Kumar Sahoo
