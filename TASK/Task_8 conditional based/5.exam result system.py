"""
Task:
- Ask for roll number

If roll number exists:
    - Ask for marks
    - If marks ≥ 40:
        "Pass"
    - Else:
        "Fail"
Else:
    "Invalid roll number"

"""
valid_roll_number=[10,11,12]
roll_number=int(input("enter the roll number: "))
if roll_number in  valid_roll_number:
    mark=int(input("enter the mark :"))
    if mark>=40:
        print("Pass")
    else:
        print("Fail")
else:
    print("invalid roll number")