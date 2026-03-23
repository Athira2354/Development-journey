"""

5. Create a nested list and perform deep copy. Modify the inner list and show that the original list remains unchanged.


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