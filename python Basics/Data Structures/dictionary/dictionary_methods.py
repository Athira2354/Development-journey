"""
class dict:

    def keys(self):=> return all keys
    def values(self):=> return all values
    def items(self):=>returns both key and values
    def get(self):=>if invalid key is entered then it doesn't shows the error but it return none
    def get("email,dummy@gmail.com)
                |
                |_=> suppose there is no existing email it will return a dummy  email like dummy@gmail.com,also if dont tell it will return none


    def pop(self,key):=>remove the key value pair in the existing key

"""
employee={"id":101,"name":"aishwarya","salary":50000,"dept":"data analysist"}

for key in employee.keys():
    print(key)
for val in employee.values():
    print(val)
for key,val in employee.items():
    print(key,val)

# print(employee.get("salary"))
print(employee.get("email","dummy@gmail.com"))
print(employee.get("email"))#=>it will  return none
print(employee["salary"]) 

# pop method
employee.pop("dept")
print(employee)
employee["bonus"]=10000
employee["salary"]+=15000
print(employee)



