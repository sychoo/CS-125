# File: alpha.py
# Author: Simon Chu
# Date: 2/20/17
# Purpose: to print out the capital letter "A".

def main():

    print()
    print("Program to print out the letter 'A' ")
    print("in various sizes. ")
    print("You will enter an odd number between 3 and 21 ")
    print("Written by Simon Chu. ")
    print()

    n = input("Enter an odd number between 3 and 21: ")

    print() # for turnin
    print()

    # determine if the input is a string & print error message
    try:
        n = int(n)
    except ValueError:
        print("Error: n must be a number, not \"" + n + "\"")
        print()
        exit()

    i = float(n)

    # determine if the number is a integer & print error message
    if i % 1 != 0:
        print("Error: Please enter a whole number, not " + str(n))
        print()
        exit()

    size = int(n)
    underscoreLine = size // 2 + 1

    # determine whether the number entered is in the valid interval & print error message
    if size < 3:
        print("Error: n must be >= 3, not " + str(n))
        print()
        exit ()

    if size > 21:
        print("Error: n must be <= 21, not " + str(n))
        print()
        exit()

    # determine whether the numbers entered are odd numbers
    if size % 2 == 0:
        print("Error: n must be an odd number, not " + str(n))
        print()
        exit()
    # print the letter "A"
    else:
        print()
        print("For n = " + str(n))
        print()
        print((size - 1) * " " + "^")

        blanks = 1
        for line in range(2, size + 1):

            if line == underscoreLine:
                print((size - line) * " " + "/" + blanks * "_" + "\\")
                blanks = blanks +2

            else:

                print((size - line) * " " + "/" + blanks * " " + "\\")
                blanks = blanks + 2

    print()




main()

