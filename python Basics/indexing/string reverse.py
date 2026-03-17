# method 1

word="welcome"
result=""
for i in range(6,-1,-1):
    result=result + word[i]
print(result)


# method 2:
word=input("enter the word:")
word_length=len(word)-1
result=""

for i in range(word_length,-1,-1):
    result= result+word[i]
print(result)