class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def employee_details(self):
        print('employee_name:',self.name)
        print('employee_salary:',self.salary)
emp1=Employee('rahil',50000)
emp1.employee_details()
emp2=Employee('sahil',60000)
emp2.employee_details()