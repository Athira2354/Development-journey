"""3. Create a menu-driven program using match–case for basic arithmetic operations:
* 1 → Addition
* 2 → Subtraction
* 3 → Multiplication
* 4 → Division
"""
num1=int(input("enter num 1:"))
num2=int(input("enter num 2:"))
operator=int(input("enter the operator:"))

print("Menu")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
match operator:
    case 1:
        print("Result=",num1+num2)
    case 2:
        print("Result=",num1-num2)
    case 3:
        print("Result=",num1*num2)
    case 4:
        print("Result=",num1/num2)

    case _ :
        print("operation invalid")