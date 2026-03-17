list=[10,11,12,13,10,11,12,12,10]
num_count={num:list.count(num) for num in list}
print(num_count)


word="racecar"
ch_count={ch:word.count(ch) for ch in word}
print(ch_count)