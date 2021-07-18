def solve(n):
    return max([int(x) for x in n])



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = input().decode().strip()
        res = solve(n)
        print(res)