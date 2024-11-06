def remove_consecutive_letters(s):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return remove_consecutive_letters(s[1:])
    else:
        return s[0] + remove_consecutive_letters(s[1:])
    
string = str(input())
print(remove_consecutive_letters(string))