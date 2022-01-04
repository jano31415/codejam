
def solve(n,s):
    last = s[0]
    first = s[0]
    last_i = n
    for i,si in enumerate(s):
        if i == 0:
            continue
        if ord(si) > ord(last):
            last_i=i
            break
        elif ord(si) == ord(last) and (ord(first) == ord(si)):
            last_i=i
            break
        last = si
    return s[:last_i] + (s[:last_i][::-1])

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s=input().decode().strip()

        res=solve(n,s)
        print(res, flush=True)