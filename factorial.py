def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
no = int(input())
result = factorial(no)
print(result)