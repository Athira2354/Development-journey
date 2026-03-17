heart_rate=int(input("enter the heart rate : "))
if(heart_rate<60):
    print("low heart rate")
elif(heart_rate<=100):
    print("normal")
else:
    print("high heart rate")