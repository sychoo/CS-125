# File: trig.py
# Author: Simon Chu
# Date: March 29 2017
# Purpose: use infinite series given to
#          calculate sin and cos of x

from math import *

def intro():
    print()
    print("Program to approximate sin and cos.")
    print("You will be asked to enter an angle and")
    print("Written by Simon Chu")
    print()

def getInputs():
    angle = float(input("Enter an angle (in degrees): "))
    print()  # for turnin
    terms = int(input("Enter the number of terms to use: "))
    print()
    print()  # for turnin
    return angle, terms


def factorial(n):
    fact = 1
    for num in range(n, 0, -1):
        fact = fact * num
    return fact


def sinCalc(x, terms):
    times = 0
    approxSin = 0
    for n in range(1, 2 * terms, 2):
        times = times + 1
        if times % 2 == 1:
            fact = factorial(n)
            approxSin = approxSin + (x ** n) / fact
        if times % 2 == 0:
            fact = factorial(n)
            approxSin = approxSin - (x ** n) / fact

    actualSin = sin(x)
    differSin = abs(actualSin - approxSin)

    return approxSin, actualSin, differSin


def cosCalc(x, terms):
    times = 0
    approxCos = 1
    for n in range(2, 2 * terms - 1, 2):
        times = times + 1
        if times % 2 == 1:
            fact = factorial(n)
            approxCos = approxCos - (x ** n) / fact
        if times % 2 == 0:
            fact = factorial(n)
            approxCos = approxCos + (x ** n) / fact

    actualCos = cos(x)
    differCos = abs(actualCos - approxCos)

    return approxCos, actualCos, differCos


def printResults(angle, approxSin, approxCos, actualSin,
                actualCos, differSin, differCos):

    angle = int(angle)
    print()
    print("Function   ", "Approx. Value   ",
          "Actual Value", " " * 3, "Difference")
    print("sin(" + str(angle) + ")    ", "{0:0.12f}   {1:0.12f}   "
          "{2:0.12f}".format(approxSin, actualSin, differSin))
    print("cos(" + str(angle) + ")    ", "{0:0.12f}   {1:0.12f}   "
          "{2:0.12f}".format(approxCos, actualCos, differCos))
    print()


def main():
    intro()
    angle, terms = getInputs()
    x = angle * pi / 180.0
    print("For", terms, "terms:")
    
    approxSin, actualSin, differSin = sinCalc(x, terms)
    approxCos, actualCos, differCos = cosCalc(x, terms)
    
    printResults(angle, approxSin, approxCos, actualSin,
                actualCos, differSin, differCos)


main()

