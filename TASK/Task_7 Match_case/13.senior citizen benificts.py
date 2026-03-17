age=int(input("enter the age:"))
match age:
    case _ if age>60:
        print("eligible for senior citizen benificts")
    case _:
        print("not eligible")