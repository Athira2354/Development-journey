"""
polymorphism
-------------------
same class have same methods and different number of parameters
one name--> differnt behaviour

method overloading-Method Overloading means having multiple methods with the same name but different parameters in the same class.
method overriding-When a child class changes the behavior of a parent class method, it is called method overriding.

"""
# method overloading
class Calculator:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
calc_instance=Calculator()
print(calc_instance.add(10,20))
print(calc_instance.add(10,20,30))
print(calc_instance.add(10,20,30,40))
    