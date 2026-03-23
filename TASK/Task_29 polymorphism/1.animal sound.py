"""

Create two classes Dog and Cat. Both classes should have a method sound(). Print different sounds for each animal.

"""

class Dog:
    def sound(self):
        return "bow bow!"
class Cat:
    def sound(self):
        return "Meow!"

Animals=[Dog(),Cat()]

for animal in Animals:
    animal.sound()
print("dogs=",Animals[0].sound())
print("cats=",Animals[1].sound())
