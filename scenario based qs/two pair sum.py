
# two pair sum
nums=[2,5,7,9]
nums.sort
target=int(input("enter a number"))
left=0
right=len(nums)-1
while(left<right):
    curr_sum=nums[left]+nums[right]
    if curr_sum==target:
        print(nums[left],nums[right])
        break
    elif curr_sum<target:
        left+=1
    elif curr_sum>target :
        right-=1

# using function

def two_pair_sum(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<right):
        curr_sum=arr[left]+arr[right]
        if curr_sum==target:
            print(arr[left],arr[right])
            break
        elif curr_sum< target:
            left+=1
        elif curr_sum>target:
            right-=1

two_pair_sum([1,2,3,5,7,9],9)   