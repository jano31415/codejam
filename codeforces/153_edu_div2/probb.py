import math
def solve(m,k,a1,ak):
    nk = m//k
    n1 = m%k
    a1 -= n1
    res=0
    if a1 <= 0:
        res += abs(a1)
        if nk > ak:
            res+= nk-ak
        return res
    nk -= a1//k
    if nk > ak:
        res += nk - ak
        return res
    # res += nk - ak
    return res
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        m,k,a1,ak = [int(x) for x in input().decode().strip().split()]
        res=solve(m,k,a1,ak)
        print(res)

