def solve(arr,n):
    start = 0
    end=n-1
    minval = 1
    maxval = n
    while start < end:
        if arr[start] == minval:
            minval+=1
            start+=1
            continue
        if arr[start] == maxval:
            maxval -= 1
            start += 1
            continue
        if arr[end] == minval:
            minval+=1
            end-=1
            continue
        if arr[end] == maxval:
            maxval -= 1
            end -= 1
            continue
        return f"{start+1} {end+1}"
    return -1


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

        res = solve(arr, n)
        print(res)