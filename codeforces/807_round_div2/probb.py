import math
def solve(n,h):
    first = False
    count = 0
    for i in range(n-1):
        if h[i]!=0:
            first=True
        if first and h[i]==0:
            count+=1
    return count + sum(h) - h[-1]
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        h = [int(x) for x in input().decode().strip().split()]

        res=solve(n,h)
        print(res)

