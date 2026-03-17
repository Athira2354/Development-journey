"""
Write a Python program to display the grade of a student using the following rules:

Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Fail

"""
mark=int(input("enter the mark :"))
if(mark>=90):
    print("Grade A")
elif(mark>=75):
    print("Grade B")
elif(mark>=50):
    print("Grade C")
else:
    print("failed")
