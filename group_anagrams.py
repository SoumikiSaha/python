from collections import defaultdict


def group_anagrams(str_list):
    ans = defaultdict(list)

    for s in str_list:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

    
l = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams(l))

