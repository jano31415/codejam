def solve(n,arr):
    p =[0]*n
    mex = 0
    seen = set()
    for i,a in enumerate(arr):
        if a > 0: # -> mex > 0 -> p0 = 1
            p[i] = mex
            seen.add(p[i])
            for new_mex in range(mex+1, n):
                if new_mex not in seen:
                    mex = new_mex
                    break
        else: # mex ==0 -> p0 = -a0
            p[i] = mex-a # a = mex - pi -> pi =mex-a
            seen.add(p[i])
    return " ".join([str(x) for x in p])




import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]

        res = solve(n,arr)
        print(res)