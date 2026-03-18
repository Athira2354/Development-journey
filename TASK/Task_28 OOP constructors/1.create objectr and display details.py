# Create a class Student with a constructor that initializes name and age. Create an object and display the details.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Rahul", 20)
student1.display()