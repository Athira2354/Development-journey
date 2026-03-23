"""
Create a list of lists and perform shallow copy using slicing. Modify an element and observe the effect.

"""
original_list = [[1, 2], [3, 4], [5, 6]]
shallow_copied_list = original_list[:]
shallow_copied_list[0].append(7)
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
