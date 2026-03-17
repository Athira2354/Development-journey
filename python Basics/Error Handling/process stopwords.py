
def remove_stop_words(sentence):

    result=""

    fr=open("python Basics\\Error Handling\\stop words.txt")
    
    stop_words=[line.rstrip("\n") for line in fr]
    
    cleaned_word=[ w for w in sentence.split(" ") if w not in stop_words]

    result=" ".join(cleaned_word)

    return result
    
    print(result)
   
sentence1="machine learning is a subset of AI"

sentence2="django is one of python framework"

print(remove_stop_words(sentence2))

# print(remove_stop_words(sentence1))


assert remove_stop_words(sentence1)=="machine learning subset AI ","Test case 1  failed"

assert remove_stop_words(sentence2)=="django one python framework ","Test case 2 failed"

print("code accepted")




