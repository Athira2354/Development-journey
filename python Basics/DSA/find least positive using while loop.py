# to find the next missing number
def missing_least_positive(arr):
    arr.sort()
    for prev in range(0,len(arr)-1):
        next=prev+1
        difference=arr[next]-arr[prev]
        if difference!=1:
            print(arr[prev]+1,"is missing")

            break
    else:
        print (arr[-1]+1)
missing_least_positive([1,2,3,4])
        