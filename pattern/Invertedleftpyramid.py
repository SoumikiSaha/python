"""
Pattern:

* * * * * * 
* * * * *
* * * *
* * *
* *
*

"""


for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print(end="\n")

"""
Pattern:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""

for i in range(6, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print(end="\n")

"""
Pattern: 

6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""


for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(end="\n")
