"""
read a number 15
display fizz if num/3
display buzz if num/5
display fizzbuzz if num/15
"""

num=int(input("enter a number:"))
if(num%15==0):
    print("FIZZBUZZ")
elif(num%5==0):
    print("BUZZ")
elif(num%3==0):
    print("FIZZ")
else:
    print("invalid")
