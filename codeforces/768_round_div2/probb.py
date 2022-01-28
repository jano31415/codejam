import math
def solve(n,a):
    if len(set(a)) == 1:
        return 0
    fill = a[-1]
    diff = [0]*n
    tot_diff = 0
    for i in range(n):
        if a[i] != fill:
            tot_diff+=1
        diff[i] = tot_diff
    pointer = n-1
    tot=0
    while pointer >= 0:
        if a[pointer] != fill:
            pointer -= (n-1 - pointer)
            tot += 1
        else:
            pointer-=1
    return tot


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
        assert len(a) ==n
        res1 = solve(n, a)
        print(res1, flush=True)

