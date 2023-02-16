def solve(a,b,n,m):
    rest = min(a,b)*(n%(m+1))
    n-=n%(m+1)
    free = n//(m+1)
    cost1 = a*(n-free)
    cost2 = b*n
    return rest +min(cost1, cost2)


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split()]
        n,m = [int(x) for x in input().decode().strip().split()]

        res = solve(a,b,n,m)
        print(res)