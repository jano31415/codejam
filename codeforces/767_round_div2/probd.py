import math
def solve(n,strings):
    tot = 0





import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        strings =[]
        for _ in range(n):
            strings.append(input().decode().strip())

        res1=solve(n,strings)
        print(res1, flush=True)
