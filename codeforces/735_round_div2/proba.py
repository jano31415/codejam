def solve(n,arr):
    best = -1
    for i,x in enumerate(arr):
        if i > 0:
            new = arr[i-1] * arr[i]
            if new > best:
                best = new
        if i < n-1:
            new = arr[i+1] * arr[i]
            if new > best:
                best = new
    return best
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
        res = solve(n,arr)
        print(res)