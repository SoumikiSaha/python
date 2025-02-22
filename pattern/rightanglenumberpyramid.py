"""
pattern:

1
12
123
1234
12345

"""

for i in range(1, 6):
    for j in range(1,i+1):
        print(j, end=" ")
    print(end="\n")

"""
Pattern:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""


for i in range(1, 6):
    for j in range(1,i+1):
        print(i, end=" ")
    print(end="\n")
