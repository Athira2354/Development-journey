"""
Create a class Employee with a method work(). Create subclasses Developer and Manager that override the work() method.

"""
class Employee:
    def work(self):
        return "Employee is working."
class Developer(Employee):
    def work(self):
        return "Developer is writing code."
    
class Manager(Employee):
    def work(self):
        return "Manager is managing the team."
employees = [Developer(), Manager()]
for employee in employees:
    print(employee.work())
    