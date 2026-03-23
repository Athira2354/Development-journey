"""
Write a Python program that uses deepcopy() to copy a dictionary with nested data.

"""
import copy
original_dict = {'numbers': [1, 2, 3, 4, 5]}
deep_copied_dict = copy.deepcopy(original_dict)
deep_copied_dict['numbers'].append(6)
print("Original Dictionary:", original_dict)
print("Deep Copied Dictionary:", deep_copied_dict)
