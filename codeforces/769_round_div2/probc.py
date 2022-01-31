
import math
def solve(a,b):
    base = (a|b) - b + 1 # or costs something
    base = min(abs(a-b), base)
    anew=a
    for i in range(1,base+1):
        anew +=1
        if (anew|b) == b:
            base = min(base, i+1) # cost of or
    bnew = b
    for i in range(1,base+1):
        bnew +=1
        if (a|bnew) == bnew:
            base = min(base,i+1)# cost of or
    return base

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split()]
        res1 = solve(a,b)
        print(res1)
        # print("\n")

# print(count_price([int(x) for x in "4 6 3 2 0 8 9 1 7 5".split()]))