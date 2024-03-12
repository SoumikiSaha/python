num = [1,2,3,1]

def containsDuplicate(nums):
    hashSet = set()
    for n in nums:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False

answer = containsDuplicate(num)
print(answer)