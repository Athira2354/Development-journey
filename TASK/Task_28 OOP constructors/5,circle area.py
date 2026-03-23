"""
Create a class Circle with a constructor that takes radius. Write a method to calculate the area of the circle.
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius*self.radius
circle=Circle(5)
print('Area of Circle:',circle.calculate_area())