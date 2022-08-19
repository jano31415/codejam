def solve(a,b,c,d):
    ad = a*d
    bc = c*b
    if ad == bc:
        return 0
    if ad < bc:
        tmp = ad
        ad = bc
        bc = tmp
    # ad > bc
    if bc == 0:
        return 1
    if ad%bc == 0:
        return 1
    return 2

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        a,b,c,d = [int(x) for x in input().decode().strip().split()]
        res=solve(a,b,c,d)
        print(res)

