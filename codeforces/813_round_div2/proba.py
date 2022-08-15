def solve(n,k,p):
    res=0
    for i,pi in enumerate(p):
        if i >= k:
            return res
        if pi > k:
            res+=1
    return res

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n, k = [int(x) for x in input().decode().strip().split()]
        p = [int(x) for x in input().decode().strip().split()]
        res=solve(n,k,p)
        print(res)

