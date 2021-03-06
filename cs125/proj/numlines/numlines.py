# Files: numlines.py
# Author: Simon Chu
# Date: Apr. 19, 2017
# Purpose: read a file, make a exact copy
# except for numbering each line and count
# the number of different letters

def intro():
    print()
    print("Program to number lines in a file.")
    print("You will enter the name of a file.")
    print("The program will create an output file.")
    print("Written by Simon Chu.")
    print()

def getInput():
    filename = input("Enter name of input file:   ")
    print() # for turnin
    outFilename = filename.split('.')[0] + ".out"
    print("The name of output file is: " + outFilename)
    print()
    return filename, outFilename

def fileProcess(filename,outFilename):
    infile = open(filename, "r").read().split('\n')
    num = 1
    outfileContent = ''
    output = ''

    for line in infile:
        if line != '':
           output = "   " + str(num) + ": " + infile[num - 1] + '\n'
           num = num + 1
           outfileContent = outfileContent + output

    outfile = open(outFilename, "w")
    outfile.write(outfileContent)
    outfile.close()
    return infile, num

def countLetters(infile):
    line = ''
    for i in infile:
        line = line + i

    j = 65
    k = 97
    list = ['0'] * 26 # initialize the value of the list
    for ch in line.strip():
        l = ord(ch)
        for m in range(j,j + 26):
            if m == l:
                list[m - 65] = str(int(list[m - 65]) + 1)

        for n in range(k,k + 26):
            if n == l:
                list[n - 97] = str(int(list[n - 97]) + 1)

    return list

def printResult(list,num):

    print("Number of lines:{0:>13}".format(num - 1))

    x = 65
    for y in range(0, 26):
        print("Number of", chr(x) + "'s:{0:>15}".format(int(list[y])))
        x = x + 1

def main():
    intro()
    filename, outFilename = getInput()
    infile, num = fileProcess(filename,outFilename)
    list = countLetters(infile)
    printResult(list,num)
    print()


main()
