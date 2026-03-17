"""
read a password
if length is greater than <6 custom error is paaswword invalid


"""

password=input("enter the password:")

if len(password)<6:

    raise Exception("password invalid")
else: 
    print("login successfull")