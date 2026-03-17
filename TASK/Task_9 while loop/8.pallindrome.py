"""
Write a program to check whether a given number is a palindrome using a while loop.

"""
number=int(input("enter a number:"))
number_copy=number
result=0
while(number!=0):
    digit=number%10
    result=result*10+digit
    number=number//10
if(result==number_copy):
    print("pallindrome")
else:
    print("not pallidrome")
