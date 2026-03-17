"""
ask for pin

if pin is correct
ask for withdrawl amounr
if amount & balance= withdrawl sucess
else=ninsufficient balance
else= incorrect pin
"""
db_pin=123123
db_amount=5000

user_pin= int(input("enter the pin"))
if(db_pin==user_pin):
    amount=int(input("enter the  withdral amount: "))
    if amount<db_amount:
        print("insufficient balance")
    else:
        print("Amount withdrawl succesfull")
else:
    print("incorrect pin")