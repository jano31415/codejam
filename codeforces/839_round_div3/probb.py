def solve(a,b,c,d):
    for i in range(4):
        a,b,c,d = c,a,d,b
        if a<b and b<d and c<d and a<c:
            return "YES"
    return "NO"

import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split()]
        c,d = [int(x) for x in input().decode().strip().split()]
        print(solve(a,b,c,d))
# import time
# a=time.time()
# n=10000
# solve(n=n, dep=[[]]+[set([i+2]) for i in range(n-1)]+[set()])
# b=time.time()
# print(b-a)