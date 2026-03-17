"""
Write a Python program to print each digit of a number separately using a while loop.
"""
number=int(input("enter a number:"))

while(number>0):
    digit=number%10
    number=number//10
    print(digit)

