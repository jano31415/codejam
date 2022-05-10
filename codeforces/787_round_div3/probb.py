import math
def solve(arr):
    last = arr[-1]
    count = 0
    for i in range(2,len(arr)+1):
        # print(f" i {i}")
        x = arr[-i]
        if last == 0:
            return -1
        while x >= last:
            x = x//2
            count += 1
        last = x
    return count


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        arr = [int(x) for x in input().decode().strip().split()]

        res=solve(arr)
        print(res)

