"""
Write a program to count the number of digits in a given number using a while loop.
"""
number=int(input("enter a number: "))
count=0
while(number>0):
    digit=number%10
    number=number//10
    count+=1
print("Number of digits","=",count)

