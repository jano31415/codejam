def solve(x,px, y,py):
    if len(str(x)) + px > len(str(y)) + py:
        return ">"
    if len(str(x)) + px < len(str(y)) + py:
        return "<"
    minpxpy = min(px, py)
    px = px - minpxpy
    py = py - minpxpy
    x = x * 10**px
    y = y * 10**py
    if x > y:
        return ">"
    if x==y:
        return "="
    if x < y:
        return "<"





import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        x,px =[int(x) for x in input().decode().strip().split(" ")]
        y,py =[int(x) for x in input().decode().strip().split(" ")]

        res=solve(x,px, y,py)
        print(res, flush=True)
