"""
Write a Python program to check whether a person is eligible to vote based on age.
"""
age=int(input(" enter the age:"))
if(age>=18):
    print("eligible for voting")
else:
    print("not eligible for voting")


age=17

vote_eligiblity=("eligible" if age >18 else "not eligible")

print(f'{age} = {vote_eligiblity}')