n=4
# upper half
for row in range(n+1):
    for sp in range(1-row):
        print(" ",end="")
    for star in range(row):
        print("*", end="")
    print()
# lowe triangle
for row in range(n-2,0,-1):
    for sp in range(n-row):
        print(" ",end="")
    for star in range(row):
        print("*",end="")
    print()
 