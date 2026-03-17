fr_all_students=open("python Basics\\file\\all students.txt","r") 
fr_passed_students=open("python Basics\\file\\passed students.txt","r")


all_students_list=[line.strip("\n") for line in fr_all_students]

passed_students_list=[line.strip("\n") for line in fr_passed_students]

print("all",all_students_list)

print("passed",passed_students_list)

failed_students=set(all_students_list).difference(passed_students_list)
print("failed stdents=",failed_students)
fr_failed_students=open("failed students.txt","w")