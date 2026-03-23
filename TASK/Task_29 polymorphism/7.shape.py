"""
Create a class Shape with a method draw(). Create subclasses Square and Triangle that override the draw() method.

"""
class Shape:
    def draw(self):
        print("shape")
class Square(Shape):
    def draw(self):
        print("Drawing a square")
class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

shape = Shape()
shape.draw()  
square = Square()
square.draw() 
triangle = Triangle()
triangle.draw()  