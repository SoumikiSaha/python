# A = [-4,-1,0,2,3,3,4]
A = [1, 4, 45, 6, 10, 8]
sum = int(input())
def find_triplet(A, sum):
    for i in range(0, len(A)-2):
        fp = i
        sp = i+1
        lp = len(A)-1
        while(sp < lp):
            if (A[fp] + A[sp] + A[lp]) == sum:
                print('Triplet is: ', A[fp], ", ", A[sp], ", ", A[lp])
                return True
            elif (A[fp] + A[sp] + A[lp]) < sum:
                sp += 1
            else:
                lp -= 1
    return False

find_triplet(A, sum)

