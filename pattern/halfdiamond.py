"""
patter:

*
**
***
****
******
*****
****
***
**
*

"""


rows = 6

for i in range(rows):
    for j in range(1, i):
        print("*", end="")
    print(end="\n")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print(end="\n")