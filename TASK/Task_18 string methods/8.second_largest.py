def second_largest(num):
    s =[10,20,30,40,50]                 # input string
    num= list(map(int, s.split()))   # convert string to list of integers
    nums = list(set(num))      # remove duplicates
    nums.sort()                 # sort numbers
    
    print(nums[-2])             # second largest)
print(second_largest([10,20,30,40,50]))