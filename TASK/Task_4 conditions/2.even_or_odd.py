"""
Write a Python program to check whether a given number is even or odd.
# """
num=int(input("enter a number:"))
if(num % 2 ==0):
    print(num,"is even")
else:
    print(num,"is odd")

num=259
result=("even"if num%2==0 else "odd")
print(f'{num} is {result}')