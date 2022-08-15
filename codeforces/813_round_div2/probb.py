def solve(n):
    if n%2 == 0:
        res = []
        for i in range(1,n+1):
            res.append(2*i)
            res.append(2*i-1)
            if len(res)==n:
                break
    else:
        res = [1]
        for i in range(1,n+1):
            if len(res)==n:
                break
            res.append(2*i+1)
            res.append(2*i)

    max=0
    for i,x in enumerate(res,1):
        if abs(i-x) <= 1:
            max +=1
    # print(max)
    return " ".join([str(x) for x in res])

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res=solve(n)
        print(res)

