class Solution:
    def digit_sum(num):
        result=0
        while num>0:
            digit=num%10
            result+=digit
            num=num//10
        return result
print(Solution.digit_sum(123))