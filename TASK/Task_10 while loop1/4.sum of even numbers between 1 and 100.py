"""
Write a program to calculate the sum of even numbers between 1 and 100 using a while loop.
"""

i=1
sum=0
while i<=100:
    if(i%2==0):
        sum=sum+i
        
    i+=1
print("sum of even numbers from 1 to 100 =",sum)