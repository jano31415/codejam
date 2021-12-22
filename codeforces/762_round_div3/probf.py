import math
from heapq import heapify,heappush,heappop


def solve(n, m, k):
    if n%m == 0:
        nm = n//m
        players = [str(i + 1) for i in range(n)]
        for game in range(k):
            cur = 0
            for i in range(m):
                l = [str(nm)] + players[cur:cur + nm]
                print(" ".join(l))
                cur += nm
        return
    else:
        nm = n//m + 1 if n%m != 0 else n//m
        shift = n%m * nm
        big_table = n%m
        players = [str(i+1) for i in range(n)]
        for game in range(k):
            cur=0
            for i in range(big_table):
                l=[str(nm)] + players[cur:cur+nm]
                print(" ".join(l))
                cur+=nm
            small_table = m - big_table
            for i in range(small_table):
                l=[str(nm-1)] + players[cur:cur+nm-1]
                print(" ".join(l))
                cur+=nm-1
            players_new = players[:]
            for i,p in enumerate(players):
                players_new[(i+shift)%n] = p
            players = players_new





import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,m,k = [int(x) for x in input().decode().strip().split(" ")]
        solve(n,m,k)
        print("", flush=True)