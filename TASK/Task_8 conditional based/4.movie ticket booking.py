"""
Task:
- Ask for age

If age ≥ 18:
    - Ask for seat availability
    - If seats available:
        "Ticket booked"
    - Else:
        "House full"
Else:
    "Not eligible to watch the movie"



"""

age=int(input("enter the age:"))

if age>=18:
    seat_availablity= input("enter the seat availablity?(yes/no)")
    if(seat_availablity=="yes"):
        print("ticket booked")
    else:
        print("Housefull")
else:
    print("Not able to watch movie")


