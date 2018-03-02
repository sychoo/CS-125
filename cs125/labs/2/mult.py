############################################################################
#
#  PROGRAM:  mult.py  -  Multiplications
#
#  AUTHOR:   Simon Chu
#
#  DATE:     January 26, 2017
#
#  FOR:      CS-125
#            Wilkes University
#
#  PURPOSE:  This Python program will ask the user to enter a number,
#            then output 2x, 4x, and 8x that number.
#
#  SPECIFICATION:
#           Input (keyboard): aNumber, an integer
#           Output (screen): 2x, 4x, and 8x aNumber
#
############################################################################
 
def main():
    # ask the user to enter an integer, storing it in the variable aNumber
    aNumber = int(input("\nPlease enter an integer: "))
 
    # output 2x, 4x, and 8x aNumber
    print ("\nTwice", aNumber, "is", 2 * aNumber, "\nand four times is",
    4 * aNumber, "\nand eight times is ", 8 * aNumber, ".\n")
 
main()
 
