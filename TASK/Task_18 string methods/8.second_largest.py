def second_largest(num):
    s =[10,20,30,40,50]                 # input string
    n = list(map(int, s.split()))   # convert string to list of integers
    nums = list(set(num))      # remove duplicates
    nums.sort()                 # sort numbers
    
    print(nums[-2])             # second largest

second_largest(num)