word1="listen"
word2="silent"
is_anagram=True
for ch in word1:
    # for ch in word2:
        if word1.find(ch)==word2.find(ch):
            is_anagram=False
        break
print(is_anagram)   


# method 2

