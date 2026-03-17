sugar_limit=int(input("enter the fasting_sugar: "))
if(sugar_limit<100):
    print("normal")
elif(sugar_limit>=100 and sugar_limit<=125 ):
    print("pre-diabetic")
elif(sugar_limit>=126):
    print("diabetic")
else:
    print("Non diabetic")
