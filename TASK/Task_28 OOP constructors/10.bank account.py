"""
10. Create a class BankAccount with a constructor that initializes account holder name and balance. Display the account details.

"""
class BankAccount:
    def __init__(self, account_holder_name, balance):
        self.account_holder_name = account_holder_name
        self.balance = balance

    def display_account_details(self):
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Balance: ${self.balance:.2f}")
account1 = BankAccount("Alice", 1000.50)
account1.display_account_details()