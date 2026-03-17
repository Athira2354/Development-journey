db_username = "admin"
db_password = 321123

username = input("Enter username: ")
if db_username==username:
    password=int(input("enter password"))
    if password==db_password:
        print("login successfull")
    else:
        print("password incorrect")
else:
    print("invalid credentials")
