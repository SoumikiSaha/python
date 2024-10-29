import re
def is_pal(S):
    word = re.sub(r'\W+?', '', S).lower()
    l , r = 0, len(word)-1
    while l < r:
        if word[l] != word[r]:
            return False
        l , r = l+1, r-1
    return True

S = "no i dont want her to leave"
if is_pal(S):
    print("Yes")
else:
    print("False")