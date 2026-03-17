class GrandParents:
    def properties(self):
        print("Grand parent properties")
class Parents(GrandParents):
    def  house(self):
        print("parents house")
class Child(Parents):
    pass

child_instance=Child()
child_instance.house()
child_instance.properties()
    