"""
Task:
- Ask for coupon code

If coupon code is valid:
    - Ask for cart amount
    - If amount ≥ 1000:
        "Coupon applied"
    - Else:
        "Minimum purchase not met"
Else:
    "Invalid coupon"



"""
db_coupen_code="AZMYNT120"

coupen_code=input("enter the coupen_code: ")

if db_coupen_code==coupen_code :
    cart_amount=int(input("enter  the cart_amount:"))
    if cart_amount>=1000:
        print("Coupen Applied")
    else:
        print("Minimum Purchase not met")
else:
    print("Invalid Coupen")