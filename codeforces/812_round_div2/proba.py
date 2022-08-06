def solve(n,coord):
    ym = [abs(x[1]) for x in coord if x[0] == 0 and x[1] < 0]
    if len(ym) == 0:
        ymax = 0
    else:
        ymax = max(ym)

    yp = [abs(x[1]) for x in coord if x[0] == 0 and x[1] > 0]
    if len(yp) == 0:
        ymin = 0
    else:
        ymin = max(yp)

    xm = [abs(x[0]) for x in coord if x[1]==0 and x[0] < 0]
    if len(xm) == 0:
        xmax =0
    else:
        xmax = max(xm)

    xp = [abs(x[0]) for x in coord if x[1] == 0 and x[0] > 0]
    if len(xp) == 0:
        xmin =0
    else:
        xmin = max(xp)
    return (ymax + xmax + xmin + ymin)*2

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        coord = []
        for i in range(n):
            xi,yi = [int(x) for x in input().decode().strip().split()]
            coord.append((xi,yi))
        res=solve(n,coord)
        print(res)

