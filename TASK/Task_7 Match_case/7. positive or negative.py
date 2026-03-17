number= int(input("enter a number: "))
match number:
    case 0: 
        print(number,"is zero")
    case _ if number>0:
        print(number, "is positive")
    case _ :
        print(number,"is negative")