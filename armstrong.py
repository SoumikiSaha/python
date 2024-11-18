def armstrong(n):
    psum = 0
    for i in str(n):
        psum += int(i) ** len(str(n))
    if psum == n:
        return True
    return False

print(armstrong(1634))