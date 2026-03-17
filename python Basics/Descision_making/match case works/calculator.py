num1=int(input("enter number 1:"))
num2= int(input("enter number 2:"))
operation=input("enter operator:")
match operation:
    case "+" :
        print(num1+num2)
    case "-" :
        print(num1 - num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case "//":
        print(num1//num2)
    case "%":
        print(num1%num2)
    case "**":
        print(num1**num2)
    case _:
        print("invalid")
