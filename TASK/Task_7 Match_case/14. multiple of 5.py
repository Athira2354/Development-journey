num=int(input("enter the number: "))
match num:
    case _ if num % 5==0:
        print(num,"is divisible by 5")
    case _ :
        print(num,"not divisible by 5")
