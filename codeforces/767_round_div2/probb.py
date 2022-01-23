import math
def solve(l,r,k):
    if l==r==1:
        return "NO"
    if r-l+1 -k <= 1:
        return "YES"
    if l%2 == 0:
        l+=1
    if math.ceil((r-l+1)/2) <= k:
        return "YES"
    return "NO"




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        l,r,k = [int(x) for x in input().decode().strip().split()]

        res=solve(l,r,k)
        print(res, flush=True)
