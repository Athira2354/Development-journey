"""
Daily Steps Activity Level
    Input: steps
    Conditions:
    If steps < 5000 → Sedentary
    If steps between 5000 and 9999 → Moderately Active
    If steps >= 10000 → Active
"""

daily_steps=int(input("enter the daily steps :"))
if(daily_steps<5000):
    print("sedentary")
elif(daily_steps<9999):
    print("Moderately Active")
else:
    print("active")