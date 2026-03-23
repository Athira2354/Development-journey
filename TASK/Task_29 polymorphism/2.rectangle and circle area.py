class Area:
    def area(self):
         print("calculating area of a shape")

class Rectangle(Area):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Area):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
rectangle = Rectangle(4, 5)
circle = Circle(3)
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())