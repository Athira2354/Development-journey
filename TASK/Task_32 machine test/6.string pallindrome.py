class Solution:
    def isPalindrome(string):
        result=False
        if string==string[::-1]:
            print(f'{string} is palindrome')
            result=True
        else:
            print(f'{string} is not palindrome')
        return result    
print(Solution.isPalindrome("malayalam"))
