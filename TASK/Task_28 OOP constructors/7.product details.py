"""
Create a class Product with a constructor that initializes product name and price. Print the product details.

"""
class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
product1 = Products("Laptop", 999.99)
product1.display_details()
product2 = Products("Smartphone", 499.99)
product2.display_details()