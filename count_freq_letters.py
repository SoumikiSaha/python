str = input("Enter a string/line:")
d = {}
for i in str:
    keys = d.keys()
    if i in keys:
        d[i] += 1
    else:
        d[i] = 1
print(d)