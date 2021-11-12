def solve(a123):
    a1,a2,a3 = a123
    amean = a1+a3
    a2 = 2*a2
    if abs(amean-a2)%3 == 0:
        return 0
    return 1

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        a123 =[int(x) for x in input().decode().strip().split(" ")]
        res=solve(a123)
        print(res, flush=True)
