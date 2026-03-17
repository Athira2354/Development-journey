num= int(input("enter a number: "))

while(num!=0):
    last_digit=num%10
    if last_digit%2==0:
        print(last_digit)
    num=num//10

    
