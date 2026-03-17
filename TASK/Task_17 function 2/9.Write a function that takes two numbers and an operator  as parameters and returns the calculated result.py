def calculator(num1,num2,op="+"):
    if op=="+":
        return num1+num2    
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    elif op=="//":
        return num1//num2
    elif op=="%":
        return num1%num2
    else:
        return num1/num2
print(calculator(10,5,"+"))
print(calculator(10,5,"*"))
print(calculator(10,5,"-"))
print(calculator(10,5,"%"))
print(calculator(10,5,"//"))
print(calculator(10,5,"**"))
print(calculator(10,5,"/"))

