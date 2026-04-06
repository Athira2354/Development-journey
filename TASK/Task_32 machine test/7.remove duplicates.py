class Solution:
    def remove_duplicates(arr):
        result=[]
        for i in arr:
            result=set(result)
            result.add(i)
            result=list(result)
        return result
print(Solution.remove_duplicates([1,2,3,2,3,4,5,6,5]))

