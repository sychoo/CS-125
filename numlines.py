
def main():
    print()
    print("Program to number lines in a file.")
    print("You will enter the name of a file.")
    print("This program will create an output file.")
    print()
    fileN, outFileN = getInputs()
    long = longList()
    inFile = open(fileN, "r")
    long1 = inFile.readlines()
    length = len(long1)

    string = '   '
    for i in range(0, length):
        string = string + str(i + 1) + ": " + long1[i] + '   '

    writeFiles(string, outFileN)
    printLines(length, long, long1)


def getInputs():

    fileN = input("Enter name of input file:   ")
    #for turnin
    print()

    n = 0
    for ch in fileN:
        if ch != ".":
            n = n + 1
        else:
            break
    outFileN = fileN[0:n] + ".out"
    print("The name of output file is: " + outFileN)

    return fileN, outFileN


def longList():

    long = []
    for num in range(65, 91):
        char = [chr(num)]
        long = long + char
    for num1 in range(97, 123):
        char = [chr(num1)]
        long = long + char


    return long


def writeFiles(string, outFileN):
    outFile = open(outFileN, "w")
    outFile.write(string)


def printLines(length, long, long1):
    print()
    print("Number of lines:           ", length)
    loopChar = ''
    for ch in long1:
        loopChar = loopChar + ch


    for num in range(26):
        for ch in loopChar:

            if ch == long[num][0]:
                long[num] = long[num] + str(0)




    for num in range(26):
        for ch in loopChar:

            if ch == long[num + 26][0]:
                long[num] = long[num] + str(0)
 


    i = 0
    for char in long[0:26]:
        stringLength = len(char) - 1
        print("Number of " + char[i][0] + "'s:              " + str(stringLength))

    print()



main()