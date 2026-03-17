"""
Stress Level Indicator
    Input: stress_score (1 to 10)
    Conditions:
    If score between 1 and 3 → Low Stress
    If score between 4 and 6 → Moderate Stress
    If score between 7 and 10 → High Stress

"""
stress_level=int(input("enter the stress level : "))
if(stress_level<3):
    print("low stress")
elif(stress_level<6):
    print("moderate stress")
else:
    print("high stress")
