"""
create a function last_digit max with two parameter num1 and num2
display num1 if last digit of num1 > last digit of num2
display num2 if last digit of num2 > last digit of num1

"""
def last_digit_max(num1,num2):
    last_digit_num1=num1%10
    last_digit_num2=num2%10
    if last_digit_num1>last_digit_num2:
        print(last_digit_num1 )
    else:
        print(last_digit_num2)


last_digit_max(151,256)
last_digit_max(98,352)