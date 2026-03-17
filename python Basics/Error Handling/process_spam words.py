def spam_words_count(message):
    result=""
    fr=open("python Basics\\Error Handling\\spam_words.txt")
    spam_words=[line.rstrip("\n") for line in fr]
    cleaned_words=[ w for w in message.split(" ") if w  in spam_words]
    spam_words_count=len(cleaned_words)
    print(len(spam_words)/len(message.split(" ")*100))
    print(spam_words_count)
    return spam_words_count
    
message="you win free cash"
print(spam_words_count("you win free cash"))
print(spam_words_count("you win free cash lottery"))

assert spam_words_count(message)=="win free cash","test case 1 failed"
# assert spam_words(message)=="win free cash","test case 2 failed"
print("code accepted")
