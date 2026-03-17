number=int(input("enter a number:"))

number_length=len(str(number))

result=0

number_copy= number



while(number!=0):

    digit=number % 10

    exponent=digit ** number_length

    result=result+exponent

    number=number//10

if(number_copy==result):

    print(number_copy,"is amstrong")
else:
    print("not amstrong")
