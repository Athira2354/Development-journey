class Father:
    def coaching_skills(self):
        print("coaching skills")

    def cooking_skills(self):
        print("cooking skills")
class Mother:
    def cooking_skils(self):
        print("cooking skills")
class Child(Father,Mother):
    pass

child_instance=Child()
child_instance.cooking_skills()
child_instance.coaching_skills()