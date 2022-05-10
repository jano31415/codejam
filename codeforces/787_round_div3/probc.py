import math
def solve(s):
    n=len(s)
    srev = s[::-1]
    last1 = srev.find("1")
    if last1 == -1:
        first0 = s.find("0")
        if first0 == -1:
            return len(s)
        return first0+1
    thieves = 0
    if s[:(n-last1-1)].find("0") == -1:
        thieves += 1 #
    srest = s[(n-last1):]
    res = srest.find("0")
    if res < 0:
        res = len(srest)
    else:
        res += 1
    thieves += res
    return thieves



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        s=input().decode().strip()

        res=solve(s)
        print(res)

