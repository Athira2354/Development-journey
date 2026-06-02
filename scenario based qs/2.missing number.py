# Missing Number in Sequence
# A list contains numbers from 1 to n, but one number is missing:
# arr = [1, 2, 4, 5, 6]
# Task: Find the missing number efficiently (O(n)).
arr = [1, 2, 4, 5, 6]
n=len(arr)+1
expected_sum=n*(n+1)//2
actual_sum=sum(arr)
missing_num=expected_sum-actual_sum
print(missing_num)