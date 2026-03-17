class Shape:
    def area(self):
        print("calculating area of a shape")
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("area of sqare=",self.side**2)
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area of rectangle=",self.length*self.breadth)

square_instance=Square(5)
square_instance.area()

rectangle_instance=Rectangle(4,5)
rectangle_instance.area()