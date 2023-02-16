def solve(x,y):
    if x < y:
        y,x = x,y
    x-=y
    res = list(range(x+1)) + list(reversed(range(1,x)))
    return [a+y for a in res]


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        x,y = [int(x) for x in input().decode().strip().split()]

        res = solve(x,y)
        print(len(res))
        print(" ".join([str(a) for a in res]))