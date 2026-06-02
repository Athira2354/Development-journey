# user name Geneerator
# write a function called user_name that generates a username  from user's email the code should as the user to input an email and the code should return everything before the @ sign as their name for example,if some one enters ben@gmail.com the code should return ben as their username

def user_name(email):
    
    username=email.split("@")[0]
    return username
email=input("enter your email:")
print(f'username : ',user_name(email))