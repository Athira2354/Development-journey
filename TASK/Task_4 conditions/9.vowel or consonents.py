"""
Write a Python program to check whether a given character is a vowel or consonant.

"""
character=input("enter the character:")
if character in [ "a","e","i","o","u"]:
    print(character,"is vowel")
else:
    print(character,"is consonent")