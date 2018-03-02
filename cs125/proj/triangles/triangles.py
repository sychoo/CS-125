# File: triangles.py
# Author: Simon Chu
# Date: April 12, 2017
# Purpose: Draw Triangles.

def getInputs(result):
    baseSize = 0
    char = ''
    indent = 0
    print("Please choose an option: ")
    print(" " * 7, "1, for triangle pointing up; ")
    print(" " * 7, "2, for triangle pointing down; ")
    print(" " * 7, "3, to print the result; ")
    print(" " * 7, "4, to add a blank line; ")
    print(" " * 7, "5, to stop this program; ")

    n = input("--> ")
    p = n
    print() # for turnin
    if n == '0':
        print("Error: option # must in the range from 1 to 5. ")
        n = 0
        print()

    # determine whether the input is a valid number
    try:
        p = float(p)
    except ValueError:
        print("Error: option # must be a valid number, not \""
              + str(n) + "\".")
        n = 0
        print()

    # determine whether the input is an integer
    if float(n) != int(float(n)) and n != 0:
        print("Error: option # must be a integer, not \""
              + str(n) + "\".")
        n = 0
        print()

    if n == str(n) and n != 0:
       n = int(float(n))
       if int(float(n)) > 5 or int(float(n)) < 1:
          print("Error: option # must in the range from 1 to 5, "
                "not \""+ str(n) +"\".")
          n = 0
          print()

       # execute corresponding command
       if n == 3:
            printTriangle(n,result)
            result = ''
       elif n == 4:
             result = result + "\n"
       elif n == 5:
             print("The program has stopped. ")
             print()
             exit()
       elif n != 0:
             baseSize = int(input("Enter size of base: "))
             if baseSize % 2 == 0:
                baseSize = baseSize + 1
             print() # for turnin
             char = input("Enter character used to draw: ")
             char = char[0]
             print()  # for turnin
             indent = int(input("Enter number of blanks preceding \
each line: "))
             print()  # for turnin

    return n,baseSize,char,indent,result


def makeStripe(x,char,result):
    result = result + x * (char)
    return result

def makeIndent(y,indent,result):
    result = result + "\n" + (indent + y) * ' '
    return result

def makeTriangle(n,baseSize,indent,char,result):

    if n == 1:
        x = 1
        y = baseSize // 2
        for y in range(baseSize // 2, -1, -1):
            result = makeIndent(y,indent,result)
            result = makeStripe(x,char,result)
            x = x + 2
        print()

    if n == 2:
        x = baseSize
        y = 0
        for x in range(baseSize, 0, -2):
            result = makeIndent(y,indent,result)
            result = makeStripe(x,char,result)
            y = y + 1
        print()

    return result

def printTriangle(n,result):
    if n == 3:
        print(result)

def main():
    print()
    print("Program to draw triangles.")
    print("Written by Simon Chu.")
    print()
    result = ''
    n = 0
    x = 0
    y = 0
    while n != 5:
        n,baseSize,char,indent,result = getInputs(result)
        result = makeTriangle(n, baseSize, indent, char, result)
        printTriangle(n,result)


main()
