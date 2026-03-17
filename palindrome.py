def is_palindrome(string):

    result=False
    if string==string[::-1]:
        print("pallindrome")
        result=True
    else:
        print("palindrome")
    return result
print(is_palindrome("malayalam"))