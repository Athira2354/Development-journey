text="ihave2pen1penciloneerazer "
for ch in text:
    if ch.isdigit():
        print(ch,end="\n")
# wap a pgrm to display alphbetcount,digit_count,special character_count

word="aman##plan**pacbmg154dggcarbelike&$"
alphabet_count=0
digit_count=0
special_char_count=0

for ch in word:
    if ch.isalpha():
        alphabet_count+=1
    elif ch.isdigit():
        digit_count+=1
    elif not ch.isalnum():
        special_char_count+=1
print(f'alphabet_count=',alphabet_count)
print(f'digit_count=',digit_count)
print(f'special_char_count=',special_char_count)

