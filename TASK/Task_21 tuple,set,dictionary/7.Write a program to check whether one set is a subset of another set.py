set1={1,2,3,4,5}
set2={4,5,6,7,8,9}

print(set1)
print(set2)
if set1.issubset(set2):
    print(f'{set1}is subset of {set2}')
    
else:
    print(f'{set2}is subset of {set1}')