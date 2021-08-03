def solve(n,m):
    if n > m:
        return 0
    nbin = '{0:032b}'.format(n)
    mbin = '{0:032b}'.format(m)

    used= []
    free = []
    for i in reversed(range(len(mbin))):
        if nbin[31-i] == "1":
            used.append(2**i)
        else:
            free.append(2**i)
    # print(sum(used))
    left = m-n+1
    tmp = 0
    tot_sum = sum(free)
    for i in range(len(free)):
        if tot_sum - free[i] + tmp < left:
            # print(free[i])
            tmp += free[i]
        tot_sum -= free[i]
    return tmp

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,k)
        print(res)