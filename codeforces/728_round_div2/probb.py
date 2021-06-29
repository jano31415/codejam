def solve(n, arr):
    arr_orig = arr[:]
    arr_with_i = [(arr[i],i) for i in range(len(arr))]
    arr_with_i.sort()
    tot = 0
    for i,ai in enumerate(arr_orig):
        for aj,j in arr_with_i:
            if i == j:
                continue
            if ai*aj == (i+1) + (j+1):
                tot += 1
                # print(i+1)
                # print(j+1)
            if ai*aj > (i+1) + (n+1):
                break
    return tot//2

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for i in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,arr)
        print(res)
import random
import time
n=10**3
arr = [random.randint(0,2*n) for _ in range(n)]
time1=time.time()

solve(n,arr)
time2=time.time()
print(time2-time1)