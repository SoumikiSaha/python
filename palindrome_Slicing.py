import re
def isPalindrome(s):
    word = re.sub(r'\W+?', '', s).lower()
    reverse = word[::-1]
    if word == reverse:
        return True
    return False

S = "Was it a car or a cat I saw?"
if isPalindrome(S):
    print("Yes")
else:
    print("False")