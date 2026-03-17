"""
Task:
- Ask for unlock pattern

If pattern is correct:
    - Ask for fingerprint
    - If fingerprint matches:
        "Phone unlocked"
    - Else:
        "Fingerprint mismatch"
Else:
    "Wrong pattern"

"""
db_pattern="V"

db_fingerprint="zzzzvvzz"

user_pattern=input("enter pattern:")
if db_pattern==user_pattern:
    user_finger_print=input("enter user fingerprint:")
    if db_fingerprint==user_finger_print :
        print("phone unlocked")
    else:
        print("invalid finger print")
else:
    print("patter incorrect")