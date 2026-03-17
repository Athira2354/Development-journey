screen_hours=int(input("enter the screen hours: "))
if screen_hours<2:
    print("healthy usage")
elif screen_hours<5:
    print("moderate usage")
else:
    print("excessive usage")