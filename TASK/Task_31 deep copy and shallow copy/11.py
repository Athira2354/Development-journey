"""
Create a class object and perform shallow copy of the object using the copy module.

"""
import copy
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # marks is a list (mutable)

    def display(self):
        print("Name:", self.name, "| Marks:", self.marks)
s1 = Student("Alice", [85, 90, 95])
s2 = copy.copy(s1)
print("Before modification:")
s1.display()
s2.display()
s2.marks[0] = 100
print("\nAfter modifying shallow copy:")
s1.display()
s2.display()
