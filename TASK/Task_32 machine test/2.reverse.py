# Write a program to reverse a number (without converting to string).

class Solution:
    def reverse_number(num):
        result=0
        while(num>0):
            digit=num%10
            result=result*10+digit
            num=num//10
        return result
print(Solution.reverse_number(123))