def solve(n):
    res =[]
    if n%2==0:
        for i in range(n//2):
            res.append(str(2*i+2))
            res.append(str(2*i+1))
    else:
        for i in range((n-3)//2):
            res.append(str(2*i+2))
            res.append(str(2*i+1))
        res.append(str(n))
        res.append(str(n-2))
        res.append(str(n-1))
    return " ".join(res)

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for i in range(T):
        n = int(input().decode().strip())
        res = solve(n)
        print(res)