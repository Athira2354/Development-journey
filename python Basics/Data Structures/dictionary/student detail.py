"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
Print the student name
Update marks by adding 5 bonus marks
Add a new key grade
Check if attendance key exists


"""
student={"id":1,"name":"alan","course":"btech","mark":90,"tasks":"completed"}
# print(student["name"])
student["mark"]+=5
student["grade"]="A+"
if "attendence" in student:
    print("yes")
else:
    print("no")
print(student)
