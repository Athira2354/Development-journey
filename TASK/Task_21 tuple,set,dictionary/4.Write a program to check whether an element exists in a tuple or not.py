elements=(5,10,15,20,25,30)
print(f'numbers= {elements}')
value=int(input("enter the value:"))
if value in elements:
    print(f'{value} exists')
else:
    print(f'{value} do not exists')