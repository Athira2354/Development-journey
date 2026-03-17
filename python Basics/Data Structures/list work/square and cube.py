
"""
method 1
"""

number=[2,3,4,5,6,12,13]
sq_list=[]
cube_list=[]
for num in number:
    sq= num**2
    cube= num**3
    sq_list.append(sq)
    cube_list.append(cube)
print("square=",sq_list)
print("cube =",cube_list)

"""
method 2
"""
number=[2,3,4,5,6,12,13]
sq_list=[]
cube_list=[]
for num in number:
    # sq= num**2
    # cube= num**3
    sq_list.append(num**2)
    cube_list.append(num**3)
print("square=",sq_list)
print("cube =",cube_list)

