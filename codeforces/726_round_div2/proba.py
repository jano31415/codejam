def solve(N, arr):
    tot = sum(arr)
    if tot == N:
        return 0
    if tot < N+1:
        return 1
    if tot > N:
        return tot-N

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        N = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(N, arr)
        print(res)