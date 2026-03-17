# check usser password length is 8 char long
user_password=input("enter the password : ")
if len(user_password)<8:
    print("invalid")
else:
    print("valid")
