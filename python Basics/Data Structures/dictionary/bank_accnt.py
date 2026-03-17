"""Create a dictionary:
account_number
holder_name
balance
Tasks:
Deposit 5000
Withdraw 2000
Check if balance is less than 1000 → print "Low Balance"
"""
bank_account={"account_number":"CNB1234 4564 8974","holder_name":"anoop","balance":5000}
bank_account["balance"]+=5000
# bank_account["withdraw"]-=2000
if bank_account["balance"]>2000:
    bank_account["balance"]-=2000
else :
    print("insufficient balance")

if bank_account["balance"]  <=1000 :

    print("insufficient balance")

print(bank_account)



