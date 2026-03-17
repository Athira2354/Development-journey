"""
Write a Python program to find the largest of two numbers entered by the user.
"""
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if(num1>num2):
    print(num1,"is larger than ",num2)
elif(num2>num1):
    print(num2, "is larger than ",num1)
else:
    print(num1 ,"=",num2)

