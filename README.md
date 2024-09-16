# Mastermind Game

A command-line based **Mastermind** game where the user has to guess a randomly generated 4-digit number within 10 attempts. The program provides feedback on how many digits were correct and in the right position after each guess.

## Table of Contents
- [How to Play](#how-to-play)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [License](#license)

## How to Play

1. The program generates a random 4-digit number between 1000 and 9999.
2. You have **10 attempts** to guess the number.
3. After each guess, the game will tell you how many digits you guessed correctly and if they are in the correct position.
4. If you guess all digits correctly, you win!
5. If you fail to guess the number within 10 attempts, you lose and the correct number will be displayed.

### Input Validation
- You must input exactly a 4-digit number.
- Non-numeric inputs or numbers not exactly 4 digits long are invalid and will prompt an error message without counting as an attempt.

## Features
- Validates user input (must be a 4-digit number).
- Provides feedback after each guess on how many digits were correct.
- Limits the number of attempts to 10.
- Displays the correct number if the user fails to guess within the limit.
- Keeps track of the number of attempts made.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/mastermind-game.git
    ```
2. Navigate into the project directory:
    ```bash
    cd mastermind-game
    ```

3. Run the game using Python:
    ```bash
    python mastermind_game.py
    ```

## Usage

Once the game starts, you will be prompted to enter your guess. Here’s an example interaction:

```bash
Welcome to the Mastermind Game!
Guess the 4-digit number: 1234
Not quite the number. But you did get 1 digit(s) correct: 1XXX

Guess the 4-digit number: 5678
None of the numbers in your input match.

Guess the 4-digit number: 9876
Not quite the number. But you did get 2 digit(s) correct: 9X7X

...

Guess the 4-digit number: 1234
Great! You guessed the number in 6 tries! You're a Mastermind!
