"""

Create a class Payment with a method pay(). Create subclasses CreditCard and UPI that override the pay() method.

"""
class Payment:
    def pay(self):
        print("Payment made using Payment method.")

class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card.")

class UPI(Payment):
    def pay(self):
        print("Payment made using UPI.")
payment1 = CreditCard()
payment2 = UPI()
payment1.pay()  
payment2.pay()  

