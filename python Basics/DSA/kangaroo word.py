def kangaroo_word(word):
    word=word.lower()
    if len(word)<3:
        return False
    for i in range(1,len(word)-1):
        if word[i-1] in word and word[i+1] in word:
            return True
        return False
print(kangaroo_word("joey"))
