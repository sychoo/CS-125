# Files: checkerboard.py
# Author: Simon Chu
# Date: 4/6/2017
# Purpose: output a checkerboard based on user input.

def intro():
    print()
    print("This program will display a checkerboard.")
    print("You will enter the number of rows, columns,")
    print("block size and the checkerboard character.")
    print("Written by Simon Chu.")
    print()

def getValues():
    rows = int(input("How many rows? "))
    print() # for turnin
    cols = int(input("How many columns? "))
    print() # for turnin
    blockSize = int(input("What is the block size? "))
    print() # for turnin
    char = input("What is the checkerboard character? ")
    char = char[0]
    print() # for turnin
    print()

    return rows,cols,blockSize,char

def checkerboard(rows,cols,blockSize,char):
    for i in range(rows):
        if i % 2 == 0: # if i is even
            writeRow(cols,blockSize,char)
        else:
            writeRowIndented(cols,blockSize,char)

def writeRow(cols,blockSize,char):
    line = ""
    for c in range (cols):
        if c % 2 == 0: # c is even
            line = line + blockSize * char
        else:
            line = line + blockSize * " "

    for b in range(blockSize):
            print(line)

def writeRowIndented(cols,blockSize,char):
    line = ""
    for c in range (cols):
        if c % 2 == 1: # c is odd
            line = line + blockSize * char
        else:
            line = line + blockSize * " "

    for b in range(blockSize):
            print(line)


def main():
    intro()
    rows,cols,blockSize,char = getValues()
    checkerboard(rows,cols,blockSize,char)
    print()

main()
