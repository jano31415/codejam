import math
def solve(n,r,b):
    if b == 0:
        return "R"*r
    div = r//(b+1)
    # if r - (div * b) > div:
    #     div+=1
    # div = math.ceil(r/(b+1))
    totr = 0
    s=[]
    totb =0
    div1 = r % (b+1)
    for i in range(div1):
        s.append("R" * (div+1))
        totr+=(div+1)
        if (b+1)-div1 != 0:
            s.append("B")
        totb += 1
    for i in range((b+1)-div1):
        s.append("R" *div)
        totr+=div
        if i != (b-div1):
            s.append("B")
        totb += 1
    # if (totr-r) != 0:
    #     if r-totr > div:
    #         assert False
    #     s.append("R"* (r-totr))
    #     totr += (r-totr)
    # if totb < b:
    #     if b-totb > div:
    #         print(n,r,b)
    #         assert False
    #     s.append("B"*(b-totb))
    #     totb += (b-totb)
    res = "".join(s)
    # assert r == totr
    # assert r == res.count("R")
    # assert b == totb
    # assert b == res.count("B")

    return res


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,r,b = [int(x) for x in input().decode().strip().split()]

        res=solve(n,r,b)
        print(res)

# solve(14, 8, 6)
# import random
# for n in range(1000):
#     for x in range(1,n):
#         y = n-x
#         print(n,x,y)
#         solve(n, max(x,y), min(x,y))