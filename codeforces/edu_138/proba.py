def solve(n,m, rooks):
    if n==m:
        return "NO"
    return "YES"


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        rooks = []
        for i in range(m):
            a,b = [int(x) for x in input().decode().strip().split()]
            rooks.append((a,b))
        res=solve(n,m,rooks)
        print(res)

