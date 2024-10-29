def find_target(numbers, target):
    l , r= 0, len(numbers)-1

    while l < r:
        total = numbers[l] + numbers[r]

        if total < target:
            l += 1
        elif total > target:
            r -= 1
        else:
            return [l, r]
        
l = [1, 2, 3, 4, 5]
answer = find_target(l, 9)
print(answer)