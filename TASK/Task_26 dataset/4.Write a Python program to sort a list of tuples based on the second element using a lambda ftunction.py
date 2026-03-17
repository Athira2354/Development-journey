"""
Write a Python program to sort a list of tuples based on the second element using a lambda function.


"""
students=[
    ("hari",175),
    ("madhav",125),
    ("keshav",135),
    ("midhun",160),
    ("pranav",155),
    ("akhil",130),
    
]
print(sorted(students,key=lambda tp:tp[1], reverse=True))