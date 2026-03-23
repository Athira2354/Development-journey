"""

2. Write a program to demonstrate shallow copy using the copy module.
"""
import copy
original_list = [1, 2, [3, 4], 5]
shallow_copied_list = copy.copy(original_list)
print("Original List:", original_list)
print("Shallow Copy:", shallow_copied_list)

original_list[2][0] = 'X'
print("\nAfter modifying the nested list in the original list:")
print("Original List:", original_list)
print("Shallow Copy:", shallow_copied_list)
