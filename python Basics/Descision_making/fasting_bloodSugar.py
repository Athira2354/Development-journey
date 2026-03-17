fasting_blood_sugar=int(input("enter fasting blood_sugar: "))
if(fasting_blood_sugar<100):
    print("Normal")
elif(fasting_blood_sugar>100 and fasting_blood_sugar<125):
    print("Prediabetic")
else:
    print("Diabetis")