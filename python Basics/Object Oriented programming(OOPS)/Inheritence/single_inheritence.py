class Parent:
    def house(self):
        print("Parent class  house method")
class Child(Parent):
    def mobile(self):
        print("child class mobile method")
child_instance=Child()
child_instance.mobile()
