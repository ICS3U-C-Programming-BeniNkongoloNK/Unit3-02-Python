#!/usr/bin/env python3
# Created By: Beni
# Date: March 3, 2025
# Calculates the circumference of a circle

import constants

def main():
    # asks user to guess a number and sets variable guess to that number
    guess = float(input("Hello, try guessing my number: "))

    # If you get the right number
    if guess == constants.CORRECT_NUMBER:
        print("You got it!! Well done!")

    # If you get the wrong number
    if guess != constants.CORRECT_NUMBER:
        print("Sorry! The correct number was {}" .format(constants.CORRECT_NUMBER) )
        
if __name__ == "__main__":
    main()
