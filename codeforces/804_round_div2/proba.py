import math
def solve(n):
    if n%2 == 1:
        return -1
    n = n//2
    flip = {"1":"0", "0":"1"}
    bstr = "{0:b}".format(n)
    same = "".join([x for x in bstr])
    opp = "".join(["0" for x in bstr])
    opp_int = int(opp, 2)
    same_int = int(same,2)
    a1 = opp_int^opp_int
    a2 = same_int^opp_int
    a3 = opp_int^same_int

    assert a1+a2+a3 == 2*n
    return " ".join([str(a1), str(a2), str(a3)])

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        res=solve(n)
        print(res)

