def differenceofSum(n,m):
    divisible_by_m = 0
    not_divisible_by_m = 0
    for i in range(1, n+1):
        if i % m == 0:
            divisible_by_m += i
        else:
            not_divisible_by_m += i
    return not_divisible_by_m - divisible_by_m

m = 6
n = 30
print(differenceofSum(n, m))
