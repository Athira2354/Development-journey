""" 
poor=300-550
average=550-650
good= 650-750
excellent=750-900
"""

cibl_score=int(input("enter the cibil score :"))
if(cibl_score>=300 and cibl_score<550):
    print("Poor")
elif(cibl_score>=550 and cibl_score<650):
    print("average")
elif(cibl_score>=650 and cibl_score<750):
    print("good")
else:
    print("excellent")