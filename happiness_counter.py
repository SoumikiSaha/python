# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

user_input = input()
happy_len , list_len = user_input.split()
happy_numbers = input().split()
A = input().split()
B = input().split()
happiness = 0
for i in range(0, int(list_len)):
    if A[i] in happy_numbers:
        happiness += 1
    if B[i] in happy_numbers:
        happiness -= 1
print(happiness)