"""
Create two classes Car and Bike. Both classes should have a method start() that prints different messages.

"""
class Vehicle:
    def start(self):
        return "Vehicle is starting."
class Car(Vehicle):
    def start(self):
        return "Car is starting."
class Bike:
    def start(self):
        return "Bike is starting."
vehicles=[Car(),Bike()]
for vehicle in vehicles:
    print(vehicle.start())
