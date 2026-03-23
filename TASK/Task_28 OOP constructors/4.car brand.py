"""
Create a class Car with a constructor that initializes brand and model. Print the car details using a method.
"""
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def car_details(self):
        print('car_brand:',self.brand)
        print('car_model:',self.model)
car1=Car('Toyota','Camry')
car1.car_details()
car2=Car('Honda','Civic')
car2.car_details()
car3=Car('Ford','Mustang')
car3.car_details()
        