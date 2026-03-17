num=int(input("enter the number:"))
match num:
    case _ if num>100:
        print(num,"is greater than 100")
    case _:
        print(num,"is less than 100")