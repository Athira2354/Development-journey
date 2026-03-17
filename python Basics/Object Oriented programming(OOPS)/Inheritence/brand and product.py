class Brand:
    def __init__(self,brand_name):
        self.b_name=brand_name
    def display(self):
        print(self.b_name)
class Product(Brand):
    def __init__(self,brand_name,product_name,price):
        super().__init__(brand_name)
        self.product_name=product_name
        self.price=price
    def display(self):
        super().display()
        print(self.product_name)
        print(self.price)
product_instance1=Product("Nike","Sketchers",2500)
product_instance2=Product("Puma","Running shoes",3000)
product_instance1.display()
product_instance2.display()