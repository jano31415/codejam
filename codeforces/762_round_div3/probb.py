import math
def solve(n):
    tot=1
    all = set([1])
    log2n =int(math.log2(n))+1
    sqrtn = int(math.sqrt(n)) + 2
    for k in range(2, sqrtn):
        for exp in range(2, log2n):
            mult = k**exp
            if k**exp > n:
                break
            if exp%3 == 0 or exp%2 == 0:
                all.add(mult)
    return len(all)



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        res=solve(n)
        print(res, flush=True)
