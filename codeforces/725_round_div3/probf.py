def solve(l,r):
    return solve_one(r) - solve_one(l)
    # max_dig = len(str(r))
    # for i in range(1,max_dig+1):
    #     str(l)[:]

def solve_one(l):
    lenl = len(str(l))
    tot = 0
    for i in range(len(str(l))):
        tot+= int(str(l)[:lenl-i])
    return tot

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        l,r = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(l,r)
        print(res)