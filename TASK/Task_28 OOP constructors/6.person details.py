"""
Create a class Person with a constructor that initializes name and city. Display the information

"""
class Person:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def display_info(self):
        print('Name:',self.name)
        print('City:',self.city)
person1=Person('Alice','New York')
person1.display_info()
person2=Person('Bob','Los Angeles')
person2.display_info()