"""

                    *

                *    *   *

            *     *   *    *   *

        *   *   *    *   *   *   *

    *   *   *   *   *   *   *   *   *



"""
row=5
for i in range(1,row+1):
    for sp in range(row-i):# printing space
        print(" ",end="")
    for star in range(2*i-1):#printing star
        print("*",end="")
    print()