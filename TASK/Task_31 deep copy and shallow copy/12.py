"""
Write a Python program to perform deep copy on a class object and verify that changes in copied object do not affect the original object.

"""
import copy
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   

    def display(self):
        print("Name:", self.name, "| Marks:", self.marks)
s1 = Student("Alice", [85, 90, 95])
s2 = copy.deepcopy(s1)
print("Before modification:")
s1.display()
s2.display()
s2.marks[0] = 100
print("\nAfter modifying deep copy:")
s1.display()
s2.display()
