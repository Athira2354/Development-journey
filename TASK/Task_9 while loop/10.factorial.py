"""
10. Write a program to find the factorial of a given number using a while loop.

"""
number= int(input("enter a number:"))

i=1

result=1

while(i<=number):

    result=result*i

    i+=1

print("factorial of",number,"=",result)