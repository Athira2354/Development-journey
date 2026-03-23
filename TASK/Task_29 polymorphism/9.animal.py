"""
Create a class Animal with a method eat(). Create subclasses Lion and Cow that override the eat() method.

"""
class Animal:
    def eat(self):
        print("animal is eating food")
class Lion(Animal):
    def eat(self):
        print("lion is eating meat")
class Cow(Animal):
    def eat(self):
        print("cow is eating grass")
animal1 = Lion()
animal2 = Cow()
animal1.eat()
animal2.eat()
