# File: pi.py
# Author: Simon Chu
# Date: March 30 2017
# Purpose estimate the value of pi using summation expansion

import math

def main():
    intro()
    numTerms = getTerms()

    pi1 = 0
    pi2 = 0

    print("Pi by alternating sums    Pi by odd products")
    for term in range(numTerms):
        pi1 = pi1 + getTerm1(term)
        pi2 = pi2 + getTerm2(term)

        print("{0:10.6f}{1:27.6f}".format(pi1,pi2))

    print("For", numTerms, "terms the difference is:")
    print("{0:10.6f}{1:27.6f}".format(pi1 - math.pi, pi2 - math.pi))

    print("The actual value of pi is {0:0.11f}".format(math.pi))
    print()

def intro():
    print()
    print("Program to calculate pi by 2 methods")
    print("Written by Simon Chu")
    print()
    return

def getTerm1(term):
    if term % 2 == 0:
        sign = 1
    else:
        sign = -1

    denom = term * 2 + 1
    result = sign * 4.0 / denom
    return result

def getTerm2(term):

    denom = term * 4 + 1
    result = 8.0 / (denom * (denom + 2))

    return result

def getTerms():
    numTerms = int(input("How many terms would you like? "))
    print() # for turnin
    print()
    return numTerms


main()
