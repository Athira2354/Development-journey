"""
Write a program to check whether a given character is uppercase or lowercase.


"""
char=input("enter the character:")
match char:
    case _ if char.isupper():
        print("upper case")
    case _ if char.islower():
        print("lowercase")
    case _:
        print("invalid input")