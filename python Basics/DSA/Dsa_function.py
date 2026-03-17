def missing_least_positive(arr):
    # arr.sort()
    prev=0
    next=prev+1
   
    while(prev<=len(arr)-2):
        diff=arr[next]-arr[prev]
        if diff!=1:
            print(arr[prev]+1,"is missing")
            break
        prev+=1
        next=prev+1
missing_least_positive([1,2,4])

 