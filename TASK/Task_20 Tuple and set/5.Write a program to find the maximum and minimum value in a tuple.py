number=(10,12,14,16,18,20)
max=number[0]
min=number[0]

for num in number:
    if num>max:
        max=num
    if num<min:
        min=num
print(f"maximum value ={max}")
print(f'minimum value ={min}')