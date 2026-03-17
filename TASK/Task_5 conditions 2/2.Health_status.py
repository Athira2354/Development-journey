"""
Write a Python program using if elif else to print the health status.
Blood Pressure Category
    Input: systolic_bp
    Conditions:
    If bp < 120 → Normal
    If bp between 120 and 129 → Elevated
    If bp between 130 and 139 → High BP Stage 1
    If bp >= 140 → High BP Stage 2
"""
bp=int(input("enter your bp : "))
if(bp<120):
    print("normal")
elif(bp>=120 and bp<=129):
    print("elevate")
elif(bp>=130 and bp<139):
    print("High Bp stage:1")
else:
    print("High Bp stage:2")
