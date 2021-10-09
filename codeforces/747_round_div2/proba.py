def solve(n):
    return str(-(n-1)), str(n)



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        res = solve(n)
        # check(res)
        print(" ".join(res))
