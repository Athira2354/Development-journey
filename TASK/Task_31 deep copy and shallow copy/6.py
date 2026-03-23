"""

6. Write a program to compare shallow copy and deep copy using nested lists.
"""
import copy
original = [1, 2, [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
shallow[2][0] = 99
print("\nAfter modifying shallow copy:")
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
deep[2][1] = 77
print("\nAfter modifying deep copy:")
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
