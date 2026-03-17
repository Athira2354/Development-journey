num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
op=input("enter the operation to perform:")
match op:
    case "+":
        result=num1+num2
        print(num1,"+",num2,"=",result)   
    case "-":
        result=num1-num2
        print(num1,"-",num2,"=",result) 
    case "*":
        result=num1*num2
        print(num1,"*",num2,"=",result)
    case "%":
        result=num1%num2
        print(num1,"%",num2,"=",result)
    
