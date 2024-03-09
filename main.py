from check_word_validity import check_word_validity
import sys


def main(wordle_word):
    print(sys.argv)
    print("wordle", wordle_word)

    guessed_words = []
    turn_number = 1

    for i in range(0, 6):
        guess = input("Enter a wordle guess\t").upper()
        print("guess", guess, i)

        if guess == wordle_word:
            return print("You won the game!")

        valid_word = check_word_validity(guess)

        if not valid_word:
            is_valid = False
            print("you made a guess that is not valid")
            while is_valid is False:
                guess = input("Enter a wordle guess\t").upper()
                if guess == wordle_word:
                    return print("You won the game!")
                valid_word = check_word_validity(guess)
                if valid_word:
                    is_valid = True

    print("Sorry, you didn't win this time")



    return "nices"


main(sys.argv[1])
