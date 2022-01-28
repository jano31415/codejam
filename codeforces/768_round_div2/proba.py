import math
def solve(n,a,b):
    if len(a) == len(b) == 1:
        return a[0]*b[0]
    c = [min(a[i], b[i]) for i in range(len(a))]
    maxc = max(max(a),max(b))
    return maxc * max(c)

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        a = [int(x) for x in input().decode().strip().split()]
        b = [int(x) for x in input().decode().strip().split()]

        res1 = solve(n, a,b)
        print(res1, flush=True)

