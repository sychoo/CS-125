# File: timegap.py
# Author: Simon Chu
# Date: Sunday, 23, April, 2017
# Purpose: Calculate the time gap from a certain time
#          to a certain time

import datetime
from datetime import datetime, date, time
def main():
    print("Program to calculate the time gap.")
    print("Written by Simon Chu.")
    print()
    dateStart = input("Please enter a date you would like to start calculating (i.e. 15/9/00): ")




    dateEnd = input("Please enter a date you would like to end calculating (now by default): ")



    if dateEnd == "now" or "":
        timeGap = (datetime.utcnow() - datetime.strptime(dateStart,"%d/%m/%y")).total_seconds()
        hours = timeGap / 60 / 60
        days = hours / 24
        years = days / 365


    else:
        timeGap = (datetime.strptime(dateEnd,"%d/%m/%y") - datetime.strptime(dateStart,"%d/%m/%y")).total_seconds()
        hours = timeGap / 60 / 60
        days = hours / 24
        years = days / 365
    print()
    print("Time Since date Started")
    print(round(hours,2), "Hours")
    print(round(days, 2), "Days")
    print(round(years,2), "Years")
    print()

main()



