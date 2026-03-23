"""
Create a class Laptop with a constructor that initializes brand and RAM size. Print the laptop specifications.
"""
class Laptop:
    def __init__(self, brand, ram_size):
        self.brand = brand
        self.ram_size = ram_size

    def display_specs(self):
        print(f"Laptop Brand: {self.brand}")
        print(f"RAM Size: {self.ram_size} GB")
laptop1 = Laptop("Dell", 16)
laptop1.display_specs()
laptop2 = Laptop("HP", 8)
laptop2.display_specs()