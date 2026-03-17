number=int(input("enter number:"))
match number:
    case 0:print("zero")
    case _ if number<0:
        print("negative")
    case _ if number>0:
        print("positive")
    case _:
        print("invalid")