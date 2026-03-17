"""
1. Body Temperature Status

Input: body_temperature (°C)
Conditions:

If temperature < 36 → Low Body Temperature

If temperature between 36 and 37.5 → Normal

If temperature > 37.5 → Fever
"""

temperature=float(input("enter body temperature : "))
if temperature<36:
    print("Low Body Temperature")
elif temperature<37.5:
    print("Normal")
else:
    print("fever")


