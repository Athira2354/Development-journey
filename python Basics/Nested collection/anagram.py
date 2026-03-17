word="racecar"

# print non recurrsive character
# print recurssive character whose count>2
non_recurrsive=[ch for ch in word if word.count(ch)==1]
recursive_char={ch for ch in word if word.count(ch)>=2}
print(f'recursive_char={recursive_char}')
print(f'non recurrsive_char={non_recurrsive}')
