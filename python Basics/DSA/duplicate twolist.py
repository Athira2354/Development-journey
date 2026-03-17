list1=[10,11,12,13,14]
list2=[12,14,15,16,17]


# method 1
for num in list1:
    if num in list2:
        print(num)

# method 2

list1_set=set(list1)
list2_set=set(list2)
print(list1_set.intersection(list2_set))


# using proper algorithm
list1.sort()
list2.sort()
p1=0
p2=0
while(p1<len(list1) and p2<len(list2)):
    if list1(p1) 
