set={5,10,15,20,25,30}
print(set)
value=int(input("enter a value:"))
if value in set:
    print(f'{value} exists')
else:
    print(f'{value} does not exists')