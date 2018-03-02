# File: summer.py
# Author: Simon Chu
# Date: 2/8/17
# Purpose: Add up the first n natural numbers.

def main():
    print()
    print("Program to add up the first")
    print("n natural numbers.")
    print("Written by Simon Chu.")
    print()

    value = int(input("Enter a value for n: "))
    print()
    # for turnin
    print()

    # loop to compute the sum
    sum = 0
    for i in range(1,value + 1):

        sum = sum + i

    # using the formula to calculate the sum
    num = ((value + 1) * value) / 2

    #print the results
    print("The sum of the first", value, "numbers is ")
    print(sum)

    print("Calculated by (n + 1) n / 2 is ")
    print(num)

    print()

main()

