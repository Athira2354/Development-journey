class Solution:      
    def is_prime(num):
        result = True
    # your logic
        if (num<=1) :
            result = False
        for i in range(2,num):
            if(num%i==0):
                result=False
                break
        return result
print(Solution.is_prime(3))

