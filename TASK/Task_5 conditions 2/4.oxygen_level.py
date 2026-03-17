oxygen_level=int(input("enter the oxygen_level: "))
if oxygen_level>=95 :
    print("Normal")
elif(oxygen_level>=90 and oxygen_level<=94):
    print("mild Concern")
else:
    print("Critical")