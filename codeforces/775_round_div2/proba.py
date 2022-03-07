def solve(n,water):
    last=0
    first=0
    for i,x in enumerate(water):
        if x == 0:
            first = i-1
            break
    for i in reversed(range(n)):
        if water[i] == 0:
            last = i+1
            break
    return last-first

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        water = [int(x) for x in input().decode().strip().split()]

        res=solve(n,water)
        print(res)
