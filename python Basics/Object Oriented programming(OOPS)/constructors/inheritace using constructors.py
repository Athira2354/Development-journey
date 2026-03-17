class Language:
    def __init__(self,l_name):
        self.l_name=l_name
    def display(self):
        print(self.l_name)
class Framework(Language):
    def __init__(self,l_name,f_name):
        super().__init__(l_name)
        self.f_name=f_name
    def display(self):
        super().display()
        print(self.f_name)
f_name_instance1=Framework("Python","Django")
f_name_instance2=Framework("Python","Flask")
f_name_instance3=Framework("Javascript","Express JS")
f_name_instance4=Framework("Javascript","NodeJS")
f_name_instance1.display()
f_name_instance2.display()
f_name_instance3.display()
f_name_instance4.display()


