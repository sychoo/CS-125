# File: easter.py
# Author: Simon Chu
# Date: 2/10/17
# Purpose: calculate the exact date of easter for a certain year.

def main():
    print()
    print("This program will tell you the Easter date given a year.")
    print("Written by Simon Chu.")

    print()
    year = int(input("Please enter a year: "))

    print()
    print() # for turnin

    # computation
    num1 = year % 19
    num2 = year % 4
    num3 = year % 7
    num4 = (19 * num1 + 24) % 30
    num5 = (2 * num2 + 4 * num3 + 6 * num4 + 5) % 7

    easterDate = 22 + num4 + num5
    
    print("Easter falls on ", end='')
    
    # if statement
    if easterDate <= 31:
        print("March " + str(easterDate) + " , " + str(year) + " . ")
    else:
        print("April " + str(easterDate - 31) + " , " + str(year) + " . ")

    print()

main()



