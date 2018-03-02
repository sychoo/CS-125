# File: inches.py
# Author: Simon Chu
# Date: 2/2/17
# Purpose: List table of Inch and Centimeter Equivalents

def main():
    print()
    print("Table of Inch and Centimeter Equivalents")
    print("Written by Simon Chu")
    print()

    # convert inches to centimeters
    print("Inches    Centimeters")
    print("======    ===========")

    # loop and computation
    for inches in range(0, 101, 10):
        print("  " + str(inches) + " in    " + str (inches * 2.54))

    print()


    # convert centimeters to inches
    print("Centimeters    Inches")
    print("===========    ======")

    # loop and computation
    for centimeters in range (0,101,10):
        print("  " + str(centimeters) + " cm         " + str(centimeters * 0.3937) + " in")

    print()


main()


