def isAnagram(s, t):
    s_l = s.strip("")
    s_l = s_l.sort()
    t_l = t.strip("")
    t_l = t_l.sort()
    if s_l == t_l:
        return True
    
answer = isAnagram("anagram", "naamrag")
