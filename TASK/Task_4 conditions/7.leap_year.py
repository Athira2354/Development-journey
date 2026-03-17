"""
Write a Python program to check whether a given year is a leap year.
"""
year=int(input("enter the year:"))
if(year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")