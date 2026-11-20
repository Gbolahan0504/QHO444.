# Activity 1: Importing Modules
import random


def play_guess_the_number():
    print("Please enter the minimum value:")
    minimum = int(input())
    print("Please enter the maximum value:")
    maximum = int(input())

    # Pick a random number between the two values (both included)
    number = random.randint(minimum, maximum)

    print(f"I am thinking of a number between {minimum} and {maximum}. Can you guess what it is?")
    guess = int(input())

    # Keep asking until the guess matches the number
    while guess != number:
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print("Try again:")
        guess = int(input())

    print("Congratulations! You guessed my number!")


# Only run when this file is executed directly
if __name__ == "__main__":
    play_guess_the_number()

