import math
def solve(n, arr):
    tot=0
    for i in range(n):
        for j in range(i,n):
            tot += j-i+1
            tot += arr[i:j+1].count(0)
    return tot

def mex(b):
    bset = set(b)
    for i in range(101):
        if i not in bset:
            return i



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