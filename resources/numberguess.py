"""
Number Guesser Game

The goal of this game is to try to guess a number.
The computer will tell you whether you are too high
or too low. It will also keep count of how many tries
it took you to guess the number.
"""

import random

# This line says "Run this when you tell the script to start"
if __name__ == "__main__":
    # This line picks a random integer in the range (0, 100)
    number_to_guess = random.randint(0, 100)

    # This line creates a variable called "tries" and sets it equal to 0
    # It will be used to keep track of how many guesses were made
    tries = 0

    # This line asks the user to guess a number and then
    # stores it into a variable called "guess"
    guess = input("Please guess a number between 0-100: ")

    # This line takes what the user typed and makes sure it's an integer
    guess = int(guess)

    # Increment the number of tries
    tries = tries + 1

    # This line says "Keep doing all of these things over and over
    # again until guess is equal to the random number
    while guess != number_to_guess:

        # The following line is only displayed IF the guess is greater than the number
        if (guess > number_to_guess):
            guess = input("You were too high! Try again: ")
            # This line takes what the user typed and makes sure it's an integer
            guess = int(guess)

        # The following line is only displayed IF the guess is less than the number
        elif (guess < number_to_guess):
            guess = input("You were too low! Try again: ")
            # This line takes what the user typed and makes sure it's an integer
            guess = int(guess)

        # Increment the number of tries
        tries = tries + 1


    # This line only runs once the guessed number is correct
    # The %d means "insert the number at the end into this place"
    print("Hooray! You guessed the right number! It took you %d tries to guess %d." % (tries, number_to_guess))
