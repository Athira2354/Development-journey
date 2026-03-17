number=int(input("enter a number:"))

number_copy=number

result=0

while(number!=0):#121!=0

    digit=number%10 #1!=0 2!=0

    result=result*10+digit 

    number=number//10

if(result==number_copy):

    print("palindrome")

else:
    print("not palindrome")
