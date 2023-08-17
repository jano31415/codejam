import math
def solve(s):
    n=len(s)
    s1="("*n +")"*n
    s2 ="()"*n
    if s not in s1:
        return "YES", s1
    if s not in s2:
        return "YES", s2
    return "NO", None

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        s = input().decode().strip()
        res1,res2=solve(s)
        print(res1)
        if res2 is not None:
            print(res2)

