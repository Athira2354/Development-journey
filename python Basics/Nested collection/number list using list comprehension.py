numbers_list=[i for i in range(1,11)]

print(numbers_list)

# numbers=[2,4,6,8,10]

# create a new list that contain double of each number

list=[2,4,6,8,10]
doubles=[ i*2 for i in list]
print(doubles)
# create a list of  even number from 22 to 50
list=[num for num in range(22,51)if num %2==0] 
print(list)

# create a new list that contain word length >3
words=["apple","bat","elephant","carrot","ball","red"]
new_list=[w for w in words if len(w)>3 ]
print(new_list)
    