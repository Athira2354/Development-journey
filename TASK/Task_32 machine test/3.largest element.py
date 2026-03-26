class Solution:
    def largest_element(arr):
        if len(arr)==0:
            return None
        largest=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        return largest
print(Solution.largest_element([1,2,3,4,5]))