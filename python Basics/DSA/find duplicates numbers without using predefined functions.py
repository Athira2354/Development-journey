list=[10,11,12,11,13,15,14,13]
list.sort()
prev=0

for prev in range(0,len(list)-1):
    next=prev+1
    difference=list[next]-list[prev]
    if difference==0:
        print(list[prev])


# using function

def find_duplicates(arr):
    arr.sort()
    for prev in range(0,len(arr)-1):
        next=prev+1
        difference=arr[next]-arr[prev]
        if difference==0:
            print(arr[prev])
find_duplicates([11,12,11,13,14,13])

