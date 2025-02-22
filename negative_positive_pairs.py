arr = [4, 8, 9, -4, 1, -1, -8, -9]
pairs = []
for i in arr:
    if -i in arr:
        pairs.append(-i)
        pairs.append(i)
print(pairs)