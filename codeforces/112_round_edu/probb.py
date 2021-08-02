def solve(W,H,x1,y1,x2,y2,w,h):
    maxw = max(x1, (W-x2))
    maxh = max(y1, H-y2)
    if w <= maxw or h <= maxh:
        return 0
    if w+(x2-x1) <=W or h + (y2-y1) <= H:
        best = 10**9
        if w+(x2-x1) <=W:
            best = w - maxw
        h_move = h-maxh
        if h + (y2-y1) <= H and h_move <= best:
            best = h_move
        return best
    else:
        return -1


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        W,H=[int(x) for x in input().decode().strip().split(" ")]
        x1,y1,x2,y2=[int(x) for x in input().decode().strip().split(" ")]
        w,h=[int(x) for x in input().decode().strip().split(" ")]
        res1 = solve(W,H,x1,y1,x2,y2,w,h)
        print(res1)
