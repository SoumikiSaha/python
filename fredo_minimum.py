# number_of_elements = int(input())
# elements_list = list(input())
# # elements_list = elements.split()
# initital_total = 0
# for i in elements_list:
#     initital_total += int(i)
# average = initital_total / number_of_elements
# result = average + 1
# print(result)

def find_minimum(N, A):
    sum_A = sum(A)
    x = (sum_A // N) + 1
    return x

N = int(input().strip())
A = list(map(int, input().strip().split()))

x = find_minimum(N, A)
print(x)