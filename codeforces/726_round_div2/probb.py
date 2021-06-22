def solve(n,m,i,j):
    poss = [(1,m), (n,m), (n,1), (1,1)]
    max = -1
    max_poss = None
    for x,y in poss:
        dist = abs(x-i) + abs(y-j)
        if dist >max:
            max=dist
            max_poss = (x,y)
    opp = {(1,m):(n,1),(n,m):(1,1),(n,1):(1,m),(1,1):(n,m)}
    second = opp[max_poss]
    return [max_poss[0], max_poss[1], second[0], second[1]]

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,m,i,j = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,m,i,j)
        res = [str(x) for x in res]
        print(" ".join(res))