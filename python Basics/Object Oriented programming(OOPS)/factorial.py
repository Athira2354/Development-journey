class Factorial:
    def solution(self,num):
        fact=1
        for i in  range(1,num+1):
            fact=fact*i
        return fact
fact_instance=Factorial()
print(fact_instance.solution(5))