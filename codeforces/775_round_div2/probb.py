def solve(n,passes):
    if sum(passes) == 0:
        return 0
    if 2*max(passes) <= sum(passes):
        return 1
    return 2*max(passes) - sum(passes)

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        passes = [int(x) for x in input().decode().strip().split()]

        res=solve(n, passes)
        print(res)
