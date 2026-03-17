"""
Write a Python program to print the multiplication table of a given number using a while loop.

"""
num=int(input("enter a number:"))
i=1
while (i<=10):
    result=i*num
    print(i,"*",num,"=",result)
    i+=1