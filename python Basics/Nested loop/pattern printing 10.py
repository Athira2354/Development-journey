"""

1   2   3   4   5
1   2   3   4
1   2   3   
1   2
1


"""
for r in range(1,6):
    for c in range(1,7-r):
        print(c,end='\t')
    print()