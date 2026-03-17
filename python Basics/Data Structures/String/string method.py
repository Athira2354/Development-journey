

"""
class str:
    def capitalize(self)=> return capitalized version of input strin

    def casefold(self)=>

    def index(self,substr)=> returns the index number of substr

    def find(self,substr)=>return first index of substr
                        |
                        |
                        |_____>returns -1 if  ch is not found
    def rfind(self,substr)=> return first index of substr from right side

    def count(self,substr)=>return count of substring

    def isalpha():return true if str object is an alphabet

    def isdigit():return true if str object is digit

    def isalnum():returns true if str object contain both alphabets and numbers

    def startswith():return true if str object starts with prefix

    def endswith():return true if str object ends with prefix

    def strip(self):returns the string after removing the spaces

    def lstrip() :return string after removing space in left portion of the string
    def lrstrip() :return string after removing space in right portion of the string
   



"""

"""
capitalize
"""

word="luminar"
print(word.capitalize())# capitalize the first character of word

"""
casefold
"""

word1="LUMINAR TECHNOLAB"
print(word1.casefold()) # convert all uppercase characters to lowercase

"""
index
"""
name="Luminar technolab/tech"
#     01234567891012345
print(name.index("ch"))

"""
find
"""
print(name.find("labs"))

"""
rfind
"""
print(name. rfind("ab"))

"""
count
"""
print(name.count("tech"))

"""
isalpha()
"""
word="hello"
print(word.isalpha())

"""
isdigit()
"""
age="23"
print(age.isdigit())

"""
isalnum()
"""
password="alight123"
print(password.isalnum())

"""
startswith()
"""

name="luminar technolab kochi"
print(name.startswith('lu'))

"""
endswith()
"""
print(name.endswith("vm"))

"""
strip()
"""
print(f'left{name.strip()}right')
print(name.strip("\n"))


"""
lstrip()/ rstrip()
"""
word2="\nluminar technolab\t"
new_word=word.lstrip("\n")
new_word=new_word.rstrip("\t")


""""
string is immutable(once an object is defined it cannot be changed)
"""
text="hello world"
new_string= text.capitalize()
print(new_string)
