def reverse_digits(n):
    r = 0
    while n > 0:
        l_d = n % 10
        r = r * 10 + l_d
        n //= 10
    return r

n = int(input())
print(reverse_digits(n))