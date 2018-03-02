# File: sum.py
# Author: Simon Chu
# Date: 4/6/2017
# Purpose: find a certain sum from a list

def main():
    print()
    sum = int(input("Please enter a sum you want to find: "))
    list = input("Please enter a list you want to search for the pair(s): ").split(",")
    # Generate Var
    print("The list is: ", list)

    k = 0
    for i in range(0,len(list)):

        val = int(list[i])
        valNeed = sum - val

        for j in range(i + 1,len(list)):

            if list[j] == str(valNeed):
                k = 1
                print("Found it", val, "&", valNeed, "their positions are", i + 1, "&", str(j + 1) + ", respectively")
            else:
                break

    if k != 1:
        print("I didn't find sums that equal to", sum, "in this list!")
        print()

main()

