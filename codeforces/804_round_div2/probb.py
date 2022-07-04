import math
def solve(n,m):
    res = []
    flip = {"1":"0", "0":"1"}
    row=[]
    for j in range(m):
        row.append(str((((j+1) % 4) // 2) % 2))
    res.append(row)
    row=[]
    for j in range(m):
        row.append(str((((j + 3) % 4) // 2) % 2))
    res.append(row)
    for i in range(n-2):
        if i%2==0:
            res.append(res[-1][:])
        else:
            flipped = [flip[x] for x in res[-1]]
            res.append(flipped)
    res = [" ".join(row) for row in res]
    return res

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        res=solve(n,m)
        for r in res:
            print(r)

