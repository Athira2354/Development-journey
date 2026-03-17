"""

 calculate bmi

"""
weight_in_kg=int(input("enter weight: "))
height_in_cm=int(input("enter height : "))
height_in_meter=height_in_cm/100
bmi=weight_in_kg//(height_in_meter**2)
bmi=round(bmi)
print(bmi)

if(bmi<20):
    print("Underweight")
elif(bmi< 25):
    print("normal")
elif(bmi<30):
    print("Overweight")
else:
    print("Obese")