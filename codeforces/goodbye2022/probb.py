def solve(n,k):
    l=[]
    for i in range(n//2):
        l.append(n-i)
        l.append(i+1)
    if len(l) < n:
        l.append(n//2+1)
    return " ".join([str(x) for x in l])

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        res=solve(n,m)
        print(res)

