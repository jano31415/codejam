import math
def solve(n, arr):
    tot = 0
    count_odd = 0
    count_starter = 0
    for i in range(1,n-1):
        tot += arr[i]
        if arr[i]%2 == 1:
            count_odd += 1
        if arr[i]>=2:
            count_starter+=1
    res = tot//2

    if count_starter < 1:
        return -1
    if n == 3 and arr[1] %2 == 1:
        return -1

    res += count_odd//2 + count_odd%2
    return res

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split(" ")]
        res1 = solve(n, arr)
        print(res1)
        # print("\n")