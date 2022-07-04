import math
def solve(n,perm):
    if n == 1:
        return 1
    m = 10**9+7
    rev_perm = [0]*n
    for i in range(n):
        rev_perm[perm[i]] = i
    l = min(rev_perm[0:2])
    r = max(rev_perm[0:2])
    prod = 1
    for j in range(2,n):
        if l < rev_perm[j] and rev_perm[j] < r:
            prod = (prod * (r-l-j+1)) % m
        l = min(l, rev_perm[j])
        r= max(r, rev_perm[j])
    return prod
    
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        perm = [int(x) for x in input().decode().strip().split()]
        res=solve(n,perm)
        print(res)

