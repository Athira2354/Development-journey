"""
------------------------------------
8. Restaurant Order System
------------------------------------
Task:
- Ask for table number

If table exists:
    - Ask for food availability
    - If food available:
        "Order placed"
    - Else:
        "Item out of stock"
Else:
    "Invalid table number"



"""
tb_number=[100,101,102]

table_number= int(input("enter the table:"))

if table_number in tb_number:
    food_availablity=input("food_available?yes/no")
    if food_availablity=="yes":
        print("Order placed")
    else:
        print("out of stock")
else:
    print("invalid token number")
