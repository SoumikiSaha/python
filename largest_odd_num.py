def largest_odd(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""
 
# Driver code
s = "543210"
ans = largest_odd(s)
 
# Function call
print(ans)