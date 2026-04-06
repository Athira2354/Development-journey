class Solution:
    def frequency_count(string):
        result={}
        for i in string :
            if i in result:
                result[i]+=1
            else:
                result[i]=1
        return result
print(Solution.frequency_count("hello"))