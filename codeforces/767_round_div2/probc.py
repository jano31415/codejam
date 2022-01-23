import math
def solve(n,arr):
    # minimum range query
    last_val = {}
    for i,x in enumerate(arr):
        last_val[x] = i
    b=[]
    curr_mex = 0
    curr_set = set()
    for i,x in enumerate(arr):
        if last_val.get(curr_mex, -1) < i and (len(curr_set) != 0):
            b.append(str(curr_mex))
            curr_mex=0
            curr_set=set()
        if x == curr_mex:
            curr_mex+=1
            while curr_mex in curr_set:
                curr_mex+=1
        curr_set.add(x)
    if curr_mex >= 0:
        b.append(str(curr_mex))
    return len(b), " ".join(b)





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

        res1, res2=solve(n,arr)
        print(res1, flush=True)
        print(res2, flush=True)
