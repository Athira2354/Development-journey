
numbers = {10, 25, 50, 60, 75, 40, 30, 90}

print(numbers)

numbers = {num for num in numbers if num >= 50}

print(f'removed elements = {numbers}')