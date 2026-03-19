# 1.Write a Python program to store an integer and print its type.
age=24
print(age)
print(type(age))


#2. Write a program to store a float value and display it along with its type.
pie=3.14
print(pie,type(pie))

#2 Write a program to take a string input and print its length.

string="Malayalam"
print(f'{string}={len(string)}')



# 3
string="abc"
print(string,type(string))

# 4
is_valid=True
print(type(is_valid))

# 5.Write a program to convert an integer into a string and display both values.in python

num=15
num1=str(13)
print(num,type(num))
print(num1,type(num1))

# 6.Write a program to calculate the square of a number.

num=20
square=num**2
print(f'square of {num}={square}')


# 7.Write a program to calculate the cube of a number.
num=4
cube=num**3
print(f'cube of {num}={cube}')

#8. Write a program to find the average of three numbers.
num_1=10
num_2=20
num_3=30
average=((num_1+num_2+num_3)//3)
print(f'average= {average}')

# 9.Write a program to calculate the area of a rectangle (length × breadth).
length=6
breadth=8
area=length*breadth
print(f'area of rectangle= {area}')

#10 Write a program to calculate the simple interest using formula:
# SI = (P × R × T) / 100

principle_amount=10000
rate_of_intrest= 5
time=3
simple_intrest=(principle_amount*rate_of_intrest*time)/100
print(f'simple intrest= {simple_intrest}')