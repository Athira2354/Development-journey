"""
method overriding:
----------------------
child class redefines the methods that is already defined in parent class,


"""
class parent:
    def vehicles(self):
        print("passion pro")
    def car(self):
        print("swift")
class Child:
    def vehicle(self):
        print("Himalayan")
    def car(self):
        print("Audi 360")
child_instance=Child()
child_instance.vehicle()
child_instance.car()
