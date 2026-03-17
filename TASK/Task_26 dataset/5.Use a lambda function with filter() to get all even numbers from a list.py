"""
Use a lambda function with filter() to get all even numbers from a list.

"""

lst=[10,11,12,13,14,15]
map_even=list(filter(lambda n: n%2==0,lst))
print(map_even)


even_comp=[num for num in lst if num%2==0]
print(even_comp)

map_sqaures=list(map(lambda n:n**2,lst))
print(map_sqaures)

com_squares=[num**2 for num in lst]
print(com_squares)


map_cube=list(map(lambda n:n**3,lst))
print(map_cube)