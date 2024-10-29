N = 10
A = [2, 3, 2, 5, 2, 4, 4, 1, 1, 2, 5]
M = 7
store = {}
answer = 'NO'
for n in A:
    keys = store.keys()
    if n in keys:
        store[n] += 1
    else:
        store[n] = 1

for s in store:
    if store.get(s) == M:
        answer = 'YES'

print(answer)