def print_Nos(n):
    # without loops 1 to n
    if n > 0:
        print_Nos(n - 1)
        print(n, end=" ")
n = 10
print_Nos(n)

def ulta_print(n):
    if n > 0:
        print(n, end=" ")
        ulta_print(n - 1)

ulta_print(n)