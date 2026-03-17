"""
write a program to check whether a number is fivisible 2 and 5

"""
num=int(input("enter a number:"))
if(num % 2==0 and num%5==0):

    print(num,"is divisible by 2 and 5")

else:
    print(num,"is not divisible by 2 and 5")