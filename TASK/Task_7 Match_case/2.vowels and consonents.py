"""
Write a program that takes a character and checks whether it is a vowel or consonant using match–case.

"""

character= input("enter the character:")
match character:
    case  "a"|"e"|"i"|"o"|"u":
        print(character,"is a Vowel")
    case _ :
        print(character,"is a Consonent")