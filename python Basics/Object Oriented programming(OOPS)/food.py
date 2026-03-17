class Food:
    
    def set_food(self,tittle,category,price):

# initialising objects

        self.tittle= tittle
        self.category= category
        self.price=price
        
# attributes,instance_variable
    def display(self):
        print(self.tittle,self.category,self.price)

Biriyani_instance=Food()
Biriyani_instance.set_food("Biriyani","Veg",130)
Biriyani_instance.display()
Manthi_instance=Food()
Manthi_instance.set_food("Alpham Manthi","Non Veg",400)
Manthi_instance.display()







