# 6. Custom Sort Based on Frequency
# nums = [4, 6, 2, 6, 4, 4, 2]
# Task: Sort elements based on frequency (higher frequency first).
from collections import Counter
nums=nums = [4, 6, 2, 6, 4, 4, 2]
frequency=Counter(nums)
sorted_num=sorted(nums,key=lambda x:(-frequency[x],x))
print(sorted_num)

