binary = []
def convert_binary(n):
    if n>=1:
        convert_binary(n//2)
    binary.append(n%2)
    return binary

n = int(input())
ans = convert_binary(n)
if ans[0] == 0:
    ans.pop(ans[0])
ans = ''.join([str(_f) for _f in ans if _f])
print(ans)