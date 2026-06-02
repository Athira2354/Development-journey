# 4. First Non-Repeating Character
# s = "aabbccdeff"
# Task: Find the first non-repeating character.


from collections import Counter
s="aabbccdeff"
count=Counter(s)
for ch in s:
    if count[ch]==1:
        print(ch)
        break