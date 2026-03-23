"""
Create a class Vehicle with a method move(). Create subclasses Car and Airplane that override the move() method.
"""
class Vehicle:
    def move(self):
        print("vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("car is driving on the road")
class Airplane(Vehicle):
    def move(self):
        print("airplane is flying in the sky")
vehicle1 = Car()
vehicle2 = Airplane()
vehicle1.move()
vehicle2.move()