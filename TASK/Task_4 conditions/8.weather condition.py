"""
Write a Python program to display weather conditions based on temperature:

Above 30 → Hot
20 to 30 → Warm
Below 20 → Cold
"""
temperature=int(input("enter the temperature : "))
if(temperature>30):
    print("Hot")
elif(temperature>20 and temperature<30):
    print("Warm")
else:
    print("Cold")
