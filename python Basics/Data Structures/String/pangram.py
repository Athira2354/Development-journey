word="the quick brown fox jumps over lazy dog"
alphabets="abcdefghijklmnopqrstuvwxyz"
is_pangram=True
for ch in alphabets:
    if word.find(ch)==-1:
        is_pangram=False
    break
print(is_pangram)