import math
def solve(a,b,c,x,y):
    x = max(0, x-a)
    y = max(0, y-b)
    if x+y <= c:
        return "YES"
    return "NO"


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        a, b, c, x, y = [int(x) for x in input().decode().strip().split()]

        res=solve(a,b,c,x,y)
        print(res)

