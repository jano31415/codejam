# not solved
def solve(l,r, triple):
    left = list(range(l,r+1))
    tot = 0
    for i in left:
        if i == 0:
            continue
        group_count = 1
        for j in range(2,r//i + 2):
            if i*j < len(left):
                left[i*j]=0
                group_count+=1
        if group_count > 2:
            # then j,k is multiple of i but k does not have to be a multiple of j
            tot += (group_count * (group_count-1) * (group_count-2))// 6
    alln = r-l+1
    poss = (alln * (alln - 1) * (alln - 2)) // 6
    return poss - tot

#some how precalc this
def make_triple(n):
    triple = [0]*n
    duo = [0]*n
    for i in range(n):
        pass



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    triple = make_triple(10**5)
    for t in range(T):
        l,r = [int(x) for x in input().decode().strip().split()]
        res=solve(l,r, triple)
        print(res)

