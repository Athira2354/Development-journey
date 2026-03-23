"""
Write a Python program to perform deep copy using the deepcopy() function from the copy module.

"""
import copy
original_list = [1, 2, [3, 4], 5]
deep_copied_list = copy.deepcopy(original_list)
print("Original List:", original_list)
print("Deep Copy:", deep_copied_list)
original_list[2][0] = 'X'
print("\nAfter modifying the nested list in the original list:")
print("Original List:", original_list)
print("Deep Copy:", deep_copied_list)
