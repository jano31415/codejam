def solve(n,s):
    ones = s.count("1")
    zeros = s.count("0")
    res=[]
    for i,si in enumerate(s):
        if si == "0":
            if i+1 > zeros:
                res.append(str(i+1))
        elif si == "1":
            if i+1 <= zeros:
                res.append(str(i+1))
    if len(res) == 0:
        print(0)
        return
    print(1)
    print(f"{len(res)} " + " ".join(res))

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()
        res=solve(n,s)
