# def vowels_count(text):
#     vowels=["a","e","i","o","u"]
#     count=0
#     for ch in text:
#         if ch in vowels:
#             count+=1
#     return count

# print(vowels_count("welcome to the magic world"))


def vowels_count(text):
  
    vowels="aeiou"
    count=0

    for ch in text:
        if ch in vowels:
            count+=1
    return count

print(vowels_count("welcome to the magic world"))
