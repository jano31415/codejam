import math
def solve(n):
    if n == 1:
        return 3
    bstr = "{0:b}".format(n)
    bstr_rev = bstr[::-1]
    bstr_rev = bstr_rev + "0"
    min_0 = None
    min_1 = None
    for i,x in enumerate(bstr_rev):
        if min_0 is None:
            if x == "0":
                min_0 = i
        if min_1 is None:
            if x == "1":
                min_1 = i
    # print(min_1)
    count1 = bstr_rev.count("1")
    if min_1 != 0:
        add1 = 1 if count1==1 else 0
        return 2**min_1 + add1
    else:
        if count1 == 1:
            return 3
        else:
            return 1

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        res=solve(n)
        print(res)

