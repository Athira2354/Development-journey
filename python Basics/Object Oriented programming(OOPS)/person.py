"""
class Student:
    name:str
    course:str
    roll_no:int
    
    def set_student(self,name,course,roll_no):
        self.name=name
        self.course=course
        self.roll_no=roll_no
    def display(self):
        print(self.name,self.course,self.roll_no)
student_instance=Student()
student_instance.set_student("Aryan","Data_Science",12)
student_instance.set_student("Arjun","Full stack development",10)
student_instance.display()

"""
class student:
    def __init__(self,adm_no,name,branch):
        self.adm_no=adm_no
        self.name=name
        self.adm_no=adm_no