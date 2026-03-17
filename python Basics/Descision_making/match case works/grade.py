grade=input("enter the grade:")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print ("Average")
    case _:
        print("Failed")