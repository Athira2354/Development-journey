# Create a class Rectangle with a constructor that takes length and width. Write a method to calculate the area of the rectangle.

class Rectangle:
   
    def __init__(self, length, width):
        self.length = length
        self.width = width
   
    def calculate_area(self):
        return self.length * self.width
rect1 = Rectangle(10, 5)
print("Area of Rectangle:", rect1.calculate_area())