


def odd_even(numbers):

    largest_even = max([num for num in numbers if num % 2 == 0])
    smallest_odd = min([num for num in numbers if num % 2 != 0])

    return largest_even - smallest_odd

# Example
print(odd_even([1, 2, 4, 6]))