import math
def solve(n, arr):
    last = arr[0]
    minx = 0
    maxx=10**9
    if n==1:
        return 0
    for i in range(1,n):
        this = arr[i]
        if last < this:
            maxx = min(maxx, (last+this)/2)
        elif this < last:
            minx = max(minx, (last+this + (last+this)%2)//2)
        if minx > maxx:
            return -1
        last = this
    return int((minx+maxx)//2)


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
        res = solve(n, arr)
        print(res)
# import time
# a=time.time()
# n=10000
# solve(n=n, dep=[[]]+[set([i+2]) for i in range(n-1)]+[set()])
# b=time.time()
# print(b-a)