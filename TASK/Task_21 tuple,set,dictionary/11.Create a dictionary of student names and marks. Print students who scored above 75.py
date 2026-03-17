
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eve": 78
}

print(" students and marks:", students)

print("\nStudents who scored above 75:")

for name, marks in students.items():
    if marks > 75:
        print(f"{name}: {marks}")