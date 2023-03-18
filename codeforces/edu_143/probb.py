def solve(n,k,segments):
    segments = [(li,ri) for li, ri in segments if ri >= k and li <= k]
    if len(segments) == 0:
        return "NO"
    minr = min([ri for li,ri in segments])
    maxl = max([li for li,ri in segments])
    if minr == k and maxl == k:
        return "YES"
    return "NO"



import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]
        segments =[]
        for i in range(n):
            li, ri = [int(x) for x in input().decode().strip().split()]
            segments.append((li,ri))

        res = solve(n,k,segments)
        print(res)