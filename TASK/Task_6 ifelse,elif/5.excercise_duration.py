minutes=int(input("enter the exercise duration in minutes:"))
if minutes< 30:
    print("insuffient exercise")
elif minutes<60:
    print("Good exercise")
else:
    print("Intense Exercise")