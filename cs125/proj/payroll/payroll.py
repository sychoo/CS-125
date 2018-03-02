# File: payroll.py
# Author: Simon Chu
# Date: 4/5/2017
# Purpose: import files and compute payroll.

def intro():
    print()
    print("This program will compute payroll.")
    print("Written by Simon Chu.")
    print()

def printResults(first,last,hours,wage,num,totalGross):
    # Calculate the unknown
    hours,wage = int(hours),float(wage)
    timeHalf = 0.00
    dblTime = 0.00
    ovrTime = 0.00
    grossPay = 0.00

    
    if hours <= 40:
       regPay = wage * hours
       timeHalf = 0.00
       dblTime = 0.00
       ovrTime = 0.00
       grossPay = regPay
       totalGross = totalGross + grossPay
    if hours > 40 and hours <= 45:
       regPay = wage * 40
       timeHalf = 1.5 * wage * (hours - 40) 
       dlbTime = 0.00
       ovrTime = timeHalf
       grossPay = regPay + ovrTime
       totalGross = totalGross + grossPay
    if hours > 45:
       regPay = wage * 40
       timeHalf = 1.5 * wage * 5
       dblTime = 2.0 * wage * (hours - 45)
       ovrTime = timeHalf + dblTime
       grossPay = regPay + ovrTime
       totalGross = totalGross + grossPay

    
    print("{1:<7}{2:<12}{3:>6}{0:>3}{4:>5.2f}{0:>3}{5:>6.2f}{0:>3}\
{6:>6.2f}{0:>3}{7:>6.2f}{0:>3}{8:>6.2f}{0:>3}{9:>6.2f}".format
("$",first,last,hours,wage,regPay,timeHalf,dblTime,ovrTime,grossPay))
    return totalGross


def main():
    intro()
    filename = input("Please enter the employee file name: ")
    infile = open(filename, "r").read().split("\n")
    print() # for turnin
    print()
    print("For the file", filename)
    print()
    print("First  Last", " " * 8, "Hours  Wage   Reg Pay ",
          "TimeHalf DblTime  OvrTime GrossPay")
    print("-" * 6, "-" * 13, "-" * 5, "-" * 6, "-" * 8,
          "-" * 9, "-" * 7, "-" * 8, "-" * 8)
    num = 0
    totalGross = 0.00
    for line in infile:
        if line != '':
           first,last,hours,wage = line.split(",")
           totalGross = printResults(first,last,hours,wage,num,totalGross)
           num = num + 1
           
    avgGross = totalGross / num
    avgGross = "{0:6.2f}".format(avgGross)
    print()
    print("AVERAGE GROSS PAY  " + "-" * 49 + ">  $" + str(avgGross))
    print()    
       
main()
