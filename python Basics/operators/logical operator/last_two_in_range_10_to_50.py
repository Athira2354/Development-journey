"""
check the last two digit of number is in range of 10 to 50
"""

number=1945
last_two_digit=number % 100
is_in_range=last_two_digit >=10 and last_two_digit <= 50
print(is_in_range)