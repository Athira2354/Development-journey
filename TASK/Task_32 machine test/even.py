class Solution:
    def even_numbers(num):
        result=[]
        for i in range(1,num+1):
            if(i%2==0):
                result.append(i)
        return result
print(Solution.even_numbers(100))

    
