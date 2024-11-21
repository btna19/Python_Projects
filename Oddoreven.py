# Project-2
# odd or even game

import random

def odd_or_even():
    score = 0

    print("Welcome to the Odd or Even game! /n Guess whether the number is Odd or Even.")

    print("Type 'odd' or 'even' to guess, or 'quit' to exit the game.\n")

    while True:
        number = random.randint(1, 100)
        user_guess = input("Is it Odd or Even? ")

        if user_guess == "quit":
            print("\nThanks for playing! Your final score is {score}.")
            break
        elif user_guess not in ["odd", "even"]:
            print("Invalid input! Please type 'odd', 'even', or 'quit'.")
            continue

        if (number % 2 == 0 and user_guess == "even") or (number % 2 != 0 and user_guess == "odd"):
            print("Correct! The number was {number}.")
            score += 1
        else:
            print("Wrong! The number was {number}.")
            score -= 1

        print("Your current score is: {score}")

odd_or_even()
