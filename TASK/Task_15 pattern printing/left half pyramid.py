for row in range(6,0,-1):
    for sp in range(1,row):
        print("",end=" ")
    for col in range(1,6-row+2):
        print("*",end="")
    print()