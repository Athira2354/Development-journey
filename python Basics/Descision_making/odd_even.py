"""
read num1
check the number is divisible by 2
yes:print num is even
no:num is odd
"""
num=int(input("enter a number: "))#17
if(num % 2==0):#17%2==0 =>False
    print("even")
else:
    print("odd")