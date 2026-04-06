class Solution:
    def fib(n):
        a,b=0,1
        result=""
        for i in range(n):

            print(a,end="")
            a,b=b,a+b
        return result
print (Solution.fib(10))
    
