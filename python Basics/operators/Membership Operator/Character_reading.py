"""
read a character eg:"a"
display character is vowel if ch is a vowe;
else display ch is not vowel
"""
character=input("enter the character:")
vowel="aeiou"
if(character  in vowel ):
    print(character,"is vowel")
else:
    print(character,"is not a vowel")
