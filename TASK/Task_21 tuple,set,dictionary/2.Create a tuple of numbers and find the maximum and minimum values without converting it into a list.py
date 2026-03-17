
numbers = (2, 5, 7, 9, 11, 15)
print(numbers)
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")
