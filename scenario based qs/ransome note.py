# note="hen"
# magazine="chicken"
# magazine_count={ch:magazine.count(ch)for ch in magazine}
# for ch in note:
#     if ch in magazine_count and magazine_count[ch]>1:
#         magazine_count[ch]+=1
#     else:
#         print("not ransom")
#         break
# else:
#     print("ransome note")


# method 1
note="hen"
magazine="chicken"
magazine_count={ch:magazine.count(ch)for ch in magazine}
for ch in note :
    if ch in magazine_count and magazine_count[ch]>1:
        magazine_count[ch]+=1
    else:
        print("not ransome")
        break
else:
    print("ransome note")


# method 2
def is_ransome(note,magazine):
    for ch in note:
        if note.count(ch)>magazine.count(ch):
            return "Not ransome"
        return "Ransome Note"
print(is_ransome('ab','abb'))

def is_ransome(note,magazine):
    for ch in note:
        if note.count(ch)>magazine.count(ch):
            return "Not Ransome"
        return "Ransome"
print(is_ransome('ab','abb'))

# method 3
def check_ransome_note(note,magazine):
    magazine_freq={}
    for i in magazine:
        if i in magazine_freq:
            magazine_freq[i]+=1
        else:
            magazine_freq[i]=1
    print(magazine_freq)
    for i in note:
        if magazine_freq and magazine_freq[i]>0:
            magazine_freq[i]-=1
        else:
            return "Not ransome"
    return "Ransome"

print(check_ransome_note('ab','abb'))

    


