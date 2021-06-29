def solve(n,ci,bi,x):
    pass


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    n = int(input().decode().strip())
    ci = [int(x) for x in input().decode().strip().split(" ")]
    bi = [int(x) for x in input().decode().strip().split(" ")]
    q = int(input().decode().strip())
    x = int(input().decode().strip())

    res = solve(n,ci,bi,x)
    print(res)