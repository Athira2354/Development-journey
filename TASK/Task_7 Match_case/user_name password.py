"""
if password is incorrect:
ask for otp
if otp is correct :print login successfull
else:incorrect otp
else: incorrect password


"""
db_otp=123321
db_passsword="kala@321#"
user_password=input("enter the password:")

if db_passsword==user_password:
    user_otp=input("enter the otp")
    if db_otp==user_otp :
        print("login success")
    else:
        print("invalid otp")
else:
    print("incorrect password")