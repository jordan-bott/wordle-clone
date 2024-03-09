from check_word_validity import check_word_validity
from create_schema import create_schema
import sys


def main(wordle_word):

    wordle_word = wordle_word.upper()
    guessed_words = []

    for i in range(1, 7):
        guess = input(f"Enter wordle guess number {i}:\t").upper()

        if guess == wordle_word:
            return print("You won the game!")

        valid_word = check_word_validity(guess, guessed_words)

        if not valid_word:
            is_valid = False
            while is_valid is False:
                guess = input(f"Try guess number {i} again:\t").upper()
                if guess == wordle_word:
                    return print("You won the game!")
                valid_word = check_word_validity(guess, guessed_words)
                if valid_word:
                    is_valid = True
        guessed_words.append(guess)
        wordle_schema = create_schema(wordle_word, guess)
        print(wordle_schema)

    print("Sorry, you didn't win this time")


main(sys.argv[1])
