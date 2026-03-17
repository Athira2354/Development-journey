"""
read any number
loop till num!=0
display last digit
floor

"""

num= int(input("enter a number:")) #123
while(num!=0): #
    last_digit=num%10 #123%10==3
    print(last_digit) #3
    num=num//10 #