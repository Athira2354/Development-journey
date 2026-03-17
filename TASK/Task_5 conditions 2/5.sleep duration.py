sleep_duration=int(input("enter sleeping duration :"))
if sleep_duration<6:
    print("Sleep Deprived")
elif(sleep_duration<8):
    print("Healthy Sleep")
else:
    print("over sleep")