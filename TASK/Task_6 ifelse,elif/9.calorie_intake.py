calories=int(input("enter the calorie intake: "))
if calories<1500:
    print("low  intake")
elif calories<2500:
    print("balanced intake")
else:
    print("Excess intake")