water_intake= float(input("enter the the level of water intake in litre:"))
if water_intake<2:
    print("dehydrated")
elif water_intake<3:
    print("Adequate Intake")
else:
    print("Excess Intake")