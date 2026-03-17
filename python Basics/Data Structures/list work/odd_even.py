numbers=[-1,-1,10,11,12,13,15,-15,4,-5,-10]
neg_numbers=[]
pos_numbers=[]

for num in numbers:
    if num < 0:
        neg_numbers.append(num)
    else:
        pos_numbers.append(num)
print("negative_numbers=",neg_numbers)
print("positive_numbers =",pos_numbers)
