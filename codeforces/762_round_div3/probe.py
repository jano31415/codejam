import math
from heapq import heapify,heappush,heappop
def solve(n, seq):
    seq.sort()
    counts = [0]*(n+1)
    for x in seq:
        x= min(x,n)
        counts[x] += 1
    cum_counts =[0]*(n+1)
    cur=0
    for i,c in enumerate(counts):
        cur+=c
        cum_counts[i] = cur

    backup =[]
    heapify(backup)
    sol=[]
    tot=0
    for i in range(n+1):
        if cum_counts[max(0, i-1)] < i:
            break
        if i > 0:
            for _ in range(counts[i-1]):
                heappush(backup, 1-i)
        if i > 1:
            best_element = heappop(backup)
            tot += (i-1 + best_element)
        sol.append(counts[i]+tot)

    for i in range(n+1):
        if len(sol) > n:
            break
        sol.append(-1)
    return " ".join([str(x) for x in sol])

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        seq = [int(x) for x in input().decode().strip().split(" ")]
        res=solve(n,seq)
        print(res, flush=True)
