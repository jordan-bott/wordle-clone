from check_word_validity import check_word_validity
from create_schema import create_schema
import sys


def main(wordle_word):

    wordle_word = wordle_word.upper()
    guessed_words = []
    final_schema = ""

    for i in range(1, 7):
        guess = input(f"Enter wordle guess number {i}:\t").upper()
        valid_word = check_word_validity(guess, guessed_words)

        if not valid_word:
            is_valid = False
            while is_valid is False:
                guess = input(f"Try guess number {i} again:\t").upper()
                valid_word = check_word_validity(guess, guessed_words)
                if valid_word:
                    is_valid = True
        guessed_words.append(guess)
        wordle_schema = create_schema(wordle_word, guess)
        final_schema += f"{wordle_schema}\n"

        if guess == wordle_word:
            print(f"You won in {i} turn{'s' if i != 1 else ''}! Great job")
            print(final_schema)
            return None
        else:
            print(wordle_schema)

    print(f"Sorry, you didn't win this time\nThe word was: {wordle_word.lower()}.\n")
    print(final_schema)


main(sys.argv[1])
