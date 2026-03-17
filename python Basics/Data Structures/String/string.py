"""
string :sequence of charaacters

variable_namme=" text"

char='a'

word=jjhi
|
|
|____>word is a object of class string(jjhi)

"""

# class-is used for creating objects
address=""" address line 1"""
print(type(address))#  address is a object class string
#           |
#           |_______>object
number=123
print(type(number)) #number is a object class int
is_active=False #is active is a object of class boolean

class bottle:
    def open(self):
        print("open")
    def store(self):
        print("store")
bottle_instance=bottle()
bottle_instance.open()
bottle_instance.store()


"""

# variable calling method/object creation
variable_name=class_name
"""


