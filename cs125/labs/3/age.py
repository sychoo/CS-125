# File: age.py
# Author: Simon Chu
# Date: 2/2/17
# Purpose: To calculate the age.

def main():
    print()

    print("Program to calculate your age.")
    print("Written by Simon Chu.")
    print()

    # input user's birth info
    birthMonth = int(input("Enter the month of your birth (1-12): "))
    print() # for turnin
    birthDay = int(input("Enter the day of the month of your birth (1-31): "))
    print() # for turnin
    birthYear = int(input("Enter the year of your birth: "))
    print() # for turnin
    print()


    # set today's date
    todayMonth = 2
    todayDay = 2
    todayYear = 2017


    # compute year
    age = todayYear - birthYear
    if birthMonth > todayMonth:
        age = age - 1
    if birthMonth == todayMonth:
        if birthDay < todayDay:
            age = age - 1


    # output result
    print("Today's date is", todayMonth, "/", todayDay, "/", todayYear)
    print("Your birthday is on", birthMonth, "/", birthDay, "/", birthYear)

    # output the age
    print("Your age is", age, "years old.")

    print()
    
main()
