# 🎯 Number Guessing Game

> **Codveda Technology — Python Development Internship**  
> **Level 1 · Task 2 — Number Guessing Game**

A fun command-line Python game where the computer secretly selects a number from **1 to 100** and challenges the player to find it within a limited number of valid attempts.

## 🎮 Game Features

- 🎲 Random target number from **1–100**
- 🔢 Multiple valid guessing attempts
- ⬆️ **Too high!** feedback
- ⬇️ **Too low!** feedback
- 🎯 Correct-guess detection
- ⏳ Maximum-attempt limit
- 🛡️ Invalid-input handling
- 📏 Out-of-range validation
- 🔁 Play-again functionality
- 🧪 Automated tests with unittest

## 🎯 Codveda Requirements

| Requirement | Implementation |
|---|---|
| Random number 1–100 | ✅ |
| Multiple attempts | ✅ |
| Too high / too low feedback | ✅ |
| Correct guess ends game | ✅ |
| Maximum attempts | ✅ |
| Input validation | ✅ |
| Replay option | ✅ |

## 🕹️ Game Flow

~~~text
             🎯 Start Game
                  │
                  ▼
        Generate number 1–100
                  │
                  ▼
             Enter guess
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Too Low   Correct   Too High
        │         │         │
        └────► Try Again ◄──┘
                  │
             Attempts left?
               /                    Yes        No
              │          │
              ▼          ▼
          Keep playing  Game over
~~~

## 🧰 Tech Stack

- 🐍 Python 3
- 🎲 Python random
- 🧪 unittest
- 💻 Command-line interface
- 🌿 Git
- 🐙 GitHub

**No external Python packages are required.**

## 🚀 Run the Game

~~~bash
git clone https://github.com/Bandhan-lab/codveda-python-level1-guessing-game.git
cd codveda-python-level1-guessing-game
python3 guessing_game.py
~~~

## 🧪 Run Tests

~~~bash
python3 -m unittest discover -s tests -v
~~~

Tests cover target generation, guessing feedback, invalid input, attempt limits, deterministic gameplay scenarios, and replay behavior.

## 📁 Project Structure

~~~text
codveda-python-level1-guessing-game/
├── guessing_game.py
├── tests/
│   └── test_guessing_game.py
├── README.md
└── .gitignore
~~~

## 🧠 What This Project Demonstrates

- Python functions
- Random number generation
- Loops and conditional logic
- Input validation
- Exception handling
- Attempt/state management
- Automated testing
- Interactive CLI design
- Git/GitHub workflow

## 📌 Project Status

**Status:** ✅ Completed  
**Program:** Codveda Technology — Python Development Internship  
**Level:** 1 — Basic  
**Task:** 2 — Number Guessing Game

## 👨‍💻 Author

**Bandhan Kumar Sahoo**  
B.Tech — CSE (AI & ML)  
GITA Autonomous College, Bhubaneswar, Odisha, India

Built as part of the Codveda Technology Python Development Internship.

⭐ If you enjoy the project, consider giving the repository a star.
