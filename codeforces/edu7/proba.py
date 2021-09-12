def solve(n,s):
    for i in range(n-1):
        # for j in range(i+1,n+1):
        #     stmp = s[i:j]
        #     a=stmp.count("a")
        #     b=stmp.count("b")
        #     # print(stmp)
        #     if a==b:
        #         return i+1,j+1
        if s[i] != s[i+1]:
            return i+1, i+2
    return -1,-1

import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s=input().decode().strip()
        l,r = solve(n,s)

        print(f"{l} {r}")

