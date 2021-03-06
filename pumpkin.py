# File: pumpkin.py
# Author: Simon Chu
# Date: 3/22/2017
# Purpose: Allow the user enter the values and
#          determine whether they hit the target.

from math import *

def main():
    intro()
    inputDistance = input("Please enter a distance in feet: ")

    # determine if the input is a valid number
    try:
        inputDistance = float(inputDistance)
    except ValueError:
        print() # for turnin
        print()
        print("Error: distance must be a number, not \""
              + inputDistance + "\".")
        print()
        exit()

    inputDistance = float(inputDistance)
    print()
    print()  # for turnin

    num = 1
    while num <= 6:

        # determine if the user run out of five tries
        if num > 5:
            print("Sorry, you have run out of the pumpkins! You lose!")
            print()
            exit()

        angle, velocity, num = getInputs(num)
        angleR = angleRadian(angle)
        realDistance, error, discrepancy = calc(angleR,
            velocity, inputDistance)
        printResult(angle, velocity)

        if abs(inputDistance - realDistance) <= error:
           print("the pumpkin hit the target! You win!")
           print()
           exit()

        if discrepancy < 0:
           print("the pumpkin landed excess by",
                 str(abs(discrepancy)), "feet.")
           print()

        if discrepancy > 0:
           print("the pumpkin landed short by",
                 str(abs(discrepancy)), "feet.")
           print()

def intro():
    print()
    print("Program to allow one to launch a pumpkin.")
    print("You will enter the distance to the target.")
    print("Then you will enter an angle and a velocity.")
    print("The game will end if you have not hit the")
    print("target in 5 tries (must conserve pumpkins!).")
    print("Written by Simon Chu.")
    print()

def getInputs(num):
    angle, velocity = eval(input("Enter the angle and velocity for try #"
                                  + str(num) + ": "))
    angle, velocity = float(angle), float(velocity)
    num = num + 1
    print()
    print()  # for turnin
    return angle, velocity, num

def angleRadian(angle):
    angleR = (angle * pi) / 180.0
    return angleR

def calc(angleR, velocity, inputDistance):

    realDistance = (velocity * velocity * sin(2 * angleR)) / 32.2
    error = 0.001 * inputDistance
    discrepancy = inputDistance - realDistance
    return realDistance, error, discrepancy

def printResult(angle, velocity):
    angle, velocity = int(angle), int(velocity)
    print("For an angle of", str(angle),
          "degrees and velocity of", str(velocity) + ",")


main()

