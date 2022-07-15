import math
def solve(n,x,h):
    h.sort()
    h1 = h[:n]
    h2 = h[n:]
    for i in range(n):
        if h2[i] < h1[i]+x:
            return "NO"
    return "YES"

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,x = [int(x) for x in input().decode().strip().split()]
        h = [int(x) for x in input().decode().strip().split()]

        res=solve(n,x,h)
        print(res)

