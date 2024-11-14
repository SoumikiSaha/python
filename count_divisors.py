def count_div(n):
    count = 0
    for i in str(n):
        if not int(i) == 0:
            if n % int(i) == 0:
                count += 1
        else:
            continue
    return count

n = int(input())
print(count_div(n))