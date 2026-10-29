# Hangman Game

A small command-line Hangman game written in Python. The program selects a
hidden word, and the player guesses it one letter at a time.

## Requirements

- Python 3.x
- No third-party libraries or package installation required
- No database is used; the word list and game state are held in memory

The game uses Python's built-in `random` module to select a word.

## Run the game

Open a terminal in the project folder and run:

```powershell
python ".\Hangman _Game .py"
```

If the `python` command is not available, use the Python launcher:

```powershell
py -3 ".\Hangman _Game .py"
```

## How the game works

1. The program randomly selects a word from its built-in word list.
2. It displays each letter as an underscore and prompts for a guess.
3. Enter one letter. Input is trimmed and converted to lowercase.
4. Invalid input (anything other than one alphabetic character) is rejected
   without counting as a guess.
5. A previously guessed letter is rejected without counting again.
6. A correct guess reveals that letter everywhere it appears in the word.
7. An incorrect guess increases the incorrect-guess count. The player may
   make up to six incorrect guesses.
8. The player wins by revealing every letter before reaching the limit.
   Otherwise, the game ends and reveals the word.

## Project details

| Item | Details |
| --- | --- |
| Language | Python 3 |
| Libraries | Python standard library: `random` |
| Database | None |
| Interface | Console / terminal |
| Entry point | `Hangman _Game .py` |
