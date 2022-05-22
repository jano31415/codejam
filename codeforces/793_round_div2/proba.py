import math
def solve(n,s):
    res = 0
    start=None
    if len(set(list(s))) == 1:
        return n
    if len(s) % 2 == 1:
        res+=1
        start = s[len(s)//2]
    shalf = s[:len(s)//2]
    srev =shalf[::-1]
    if start is None:
        start = srev[0]
    for si in srev:
        if si == start:
            res += 2
        else:
            return res
    return res
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()

        res=solve(n,s)
        print(res)

