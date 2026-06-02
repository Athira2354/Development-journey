# 5. Group Anagrams
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Task: Group words that are anagrams together.
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    anagrams[key].append(word)

print(list(anagrams.values()))