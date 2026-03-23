"""
Create two classes India and USA with a method capital(). Print the capital city of each country.
"""
class Country:
    def capital(self):
        print("The capital city is not defined.")
class India(Country):
    def capital(self):
        print("The capital city of India is New Delhi.")
class USA(Country):
    def capital(self):
        print("The capital city of USA is Washington, D.C.")
countries = [India(), USA()]
for country in countries:
    country.capital()