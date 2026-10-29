import random


WORDS = ["python", "hangman", "computer", "program", "keyboard"]
MAX_INCORRECT_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word one letter at a time. You can make {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        progress = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\nWord: {progress}")
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        if guessed_letters:
            print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Correct!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nYou win! The word was: {word}")
                return
        else:
            incorrect_guesses += 1
            print("Sorry, that letter is not in the word.")

    print(f"\nYou lose! The word was: {word}")


if __name__ == "__main__":
    play_hangman()