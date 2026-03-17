class Mobile:
    def __init__(self,name,image,price,rating):
        self.name=name
        self.image=image
        self.price=price
        self.rating=rating

    def display(self):
        print(self.name,self.image,self.price,self.rating)

mobile_instance_1=Mobile("galaxy s26 ultra","s26 ultra.jpeg",56000,5)
mobile_instance_1.display()
mobile_instance_2= Mobile("Iphone 17 pro max","iphone_17 pro.jpeg",170000,5)
mobile_instance_2.display()

