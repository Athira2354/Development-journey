# class BinarySearch:
#     def solution()

# arr=[10,11,12,13,14,15]
# #    0 1    2  3  4  5
# low=0
# upper=len(arr)-1
# element=int(input("enter the element :" ))
# is_present=False

# while(low<=upper):

#     mid=(low+upper)//2
#     # print(mid,low,upper)
#     # print(element,arr[mid])
#     if(element==arr[mid]):
#         is_present=True
#         break
#     elif(element<arr[mid]):
#         upper=mid-1
#     elif(element>arr[mid]):
#         low=mid+1

# print(is_present)


class BinarySearch:
    def solution(self,arr,element):
        is_present=False
        lower=0
        upper=len(arr)-1
        while(lower<=upper):
            mid=(lower+upper)//2
            if(element==arr[mid]):
                is_present=True
                break
            elif(element<arr[mid]):
                upper=mid-1
            elif(element>arr[mid]):
                lower=mid+1
        return is_present
bs_instance=BinarySearch()
arr=[10,11,12,13,14,15]
element=12
print(bs_instance.solution(arr,element))
