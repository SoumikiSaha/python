n = int(input())
def fibonacci(n):
    if n < 0:
        return "Wrong input!"
    elif n ==1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))