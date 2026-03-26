# Write a program to count vowels and consonants in a string.
class Solution:
    def vowels_and_consonents(s):
        vowels=0
        consonents=0
        for i in s:
            if i in "aeiouAEIOU":
                vowels+=1
            else:
                consonents+=1
        return vowels,consonents
print(Solution.vowels_and_consonents("hello world"))