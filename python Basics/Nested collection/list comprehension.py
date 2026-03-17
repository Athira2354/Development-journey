#  easy way for creating a sequence from another sequence
# list=>list comprehension
# set=>set comprehension
# dictionary=>dictionary comprehension



# syntax=>[left middle right]
# [return iteration condition]


arr=[10,11,12,13,14,15,16,17,18,19,20]
square=[num**2 for num in arr]
print(square)
cube=[num**3 for num in arr]
print(cube)
add_10=[num+10 for num in arr]
print(add_10)

