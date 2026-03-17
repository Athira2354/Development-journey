
"""
Write a Python program to check username and password and display login success or failure.
"""
username="adholokham"
password="adholokham123"

valid_username=input("enter the  valid username: ")
valid_passsword=input("enter the  valid password: ")

if(valid_username ==username and valid_passsword==password):
    print("login successfull")
else:
    print("login failed")