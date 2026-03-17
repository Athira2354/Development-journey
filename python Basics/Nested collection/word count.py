text="python programming programming is simple"
words=text.split(' ')#"python","programming", "programming" "is"  "simple"
word_count={w:words.count(w) for w in words}
print(word_count)

