"""

3. Create a class Bird with a method fly(). Create subclasses Sparrow and Ostrich that override the fly() method with different behaviors.


"""

class Bird:
    def fly(self):
        return "Birds can fly."
class Sparrow(Bird):
    def fly(self):
        return "Sparrow can fly."
class Ostrich(Bird):
    def fly(self):
        return "Ostrich cannot fly."
birds=[Sparrow(),Ostrich()]
for bird in birds:
    print(bird.fly())
