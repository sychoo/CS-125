# File: sqrt.py
# Date: April 27, 2017
# Author: Simon Chu
# Purpose: approximate the square root of a number
#          using Newton's Method.

from math import sqrt

def main():
    intro()
    number, diff = getValues()
    calc, tries = calcSqrt(number, diff)
    printResults(number, diff, calc, tries)
    
def intro():
    print()
    print("This program will calculate the square root")
    print("of a number using Newton's Method.")
    print("You will enter the number and the size of the")
    print("delta between Newton's Method square root")
    print("and the real square root.")
    print("Written by Simon Chu.")
    print()

def getValues():
    number = float(input("Enter the number to find its square root: "))
    print() # for turnin
    diff = float(input("Enter the delta: "))
    print() # for turnin
    print() # for turnin
    return number, diff

def calcSqrt(number, diff):
    oldGuess = 0
    guess = number / 2
    tries = 0

    while abs(guess - oldGuess) > diff:
        oldGuess = guess
        guess = (guess + number / guess) / 2
        tries = tries + 1
    return guess, tries

def printResults(number, diff, calc, tries):
    print()
    print("For the square root of", number, "after", tries, "tries")
    print("with a delta of " + str(diff) + ":")
    print("The calculated square root is {0:0.11f}".format(calc))
    print("The real square root is       {0:0.11f}".format(sqrt(number)))
    print("The difference is            ", calc - sqrt(number))
    print()

main()
