"""
Create a dictionary containing a list as a value. Perform shallow copy and modify the list. Print both dictionaries.
"""

import copy
original_dict = {'numbers': [1, 2, 3, 4, 5]}
shallow_copied_dict = copy.copy(original_dict)
shallow_copied_dict['numbers'].append(6)
print("Original Dictionary:", original_dict)
print("Shallow Copied Dictionary:", shallow_copied_dict)

