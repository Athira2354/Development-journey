"""
Create a program using match–case that accepts a grade (A, B, C, D, F) and prints the result message.

"""
grade=input("enter the grade:")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Bad")
    case _ :
        print("Fail")
