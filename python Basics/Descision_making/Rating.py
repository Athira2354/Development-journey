"""
display unsatisfied if rating <=4.0
display neutral if rating >=4.0 to <=4.5
display satisfied if rating >=4.5

"""

rating=float(input("enter the rating: "))#4.5

if(rating <=4.0):#condition :- false

    print("unsatisfied")

elif(rating >=4.0 and rating <=4.5): #condition:-false
    print("neutral")
else:#condition:-True
    print("Satisfied")