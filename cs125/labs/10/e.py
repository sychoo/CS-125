# PROGRAM:  e.py
#
# AUTHOR:   Matt Zukoski
# MODIFIED  for python 3 by: John Koch
#           with functions
# DATE:     Oct 14, 2008
# MODIFICATION: Nov. 10, 2010, November 8, 2012
#
# FOR:      CS 125 - Wilkes University
#
# PURPOSE:  estimate the value of e using summation expansion
#           e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ....
 
import math
 
def main():
	
    intro()
    terms = getTerms()
    eSum = calculate(terms)
    printResults(eSum, terms)
	
def intro():
    print ("\nThis program will estimate e using summation expansion.\n\n")
    return
 
def getTerms():
    terms = int(input("How many terms would you like to sum? "))
    return terms
    
def calculate(terms): 
    eSum = 0
 
    for i in range(terms):
        # calculate the ith term
        term = 1.0 / factorial(i)
 
        # add this term to the sum
        eSum = eSum + term
    return eSum
    
def printResults(eSum, terms):
	
    # output our approximation of e
    print ("The approximate value of e using {0} terms is {1:.20f}.".format(terms,eSum))
	
    # output the actual value of e from the math library
    print ("The actual value of e is {0:.20f}.".format(math.e))
	
    # output the difference
    print ("The difference is {0:.20f}.".format(math.e - eSum))
	
 
def factorial(n):
    # compute n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
 
    if n < 0:
        print ("ERROR! Factorial undefined for negative values!")
        return -1
    elif n == 0:
        return 1
    else:
        product = 1
        for i in range(n, 0, -1):  # loop from n downto 1
            product = product * i
        return product
 
main()
