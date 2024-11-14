def cal_gcd(a, b):
    gcd = 0
    small = 0
    if a < b:
        small = a
    else:
        small = b
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0 and i > gcd:
            gcd = i
    return gcd

a = int(input())
b = int(input())
print(cal_gcd(a, b))