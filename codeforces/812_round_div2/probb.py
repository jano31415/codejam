import math
def solve(n,p):
    pindex = [(p[i],i) for i in range(n)]
    psort = sorted(pindex)
    l=0
    r=n-1
    for pi,i in psort:
        if p[l] != pi and p[r] != pi:
            return "NO"
        if p[l] == pi:
            l+=1
        elif p[r] == pi:
            r-=1
    return "YES"

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        p = [int(x) for x in input().decode().strip().split()]

        res=solve(n,p)
        print(res)

