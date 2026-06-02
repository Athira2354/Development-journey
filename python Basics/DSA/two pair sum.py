def two_pair(arr,target):
    arr.sort()
    left = 0
    right = len(arr)-1
    pairs = []
    while left<right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            pairs.append((arr[left],arr[right]))
            left+=1
            right-=1
        elif curr_sum<target:
            left+=1
        else:right-=1
    return pairs

print(two_pair([9,2,7,6,3,4,5],9))

# method 2
arr = [2,3,4,5]
sum = 8
for i in arr:
    for j in arr:
        if sum == i + j:
            print(i,j)