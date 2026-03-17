"""
                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *


"""


for r in range(6,0,-1):
    for sp in range(1,r):
        print(" ",end="")
    for cols in range(1,6-r+2):
        print('*',end="")
    print()
