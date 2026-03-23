"""
Write a program to check the memory address of original list and copied list using id().
"""
import copy
original_list = [1, 2, 3, 4, 5]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)
print("\nMemory Addresses:")
print("Original List ID:", id(original_list))
print("Shallow Copied List ID:", id(shallow_copied_list))
print("Deep Copied List ID:", id(deep_copied_list))
