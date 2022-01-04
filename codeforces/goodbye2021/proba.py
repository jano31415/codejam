
def solve(n,arr):

    dic = {}
    for a in arr:
        a = abs(a)
        if a not in dic:
            dic[a] = 1
        else:
            if a == 0:
                dic[a] = 1
            else:
                dic[a] = 2
    tot = 0
    for d in dic.values():
        tot+=d
    return tot

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]

        res=solve(n,arr)
        print(res, flush=True)