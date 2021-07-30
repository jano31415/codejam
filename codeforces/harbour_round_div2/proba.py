def solve(n):
    if n < 9:
        return 0
    if n == 9:
        return 1
    a=int(str(n)[:-1])
    if str(n)[-1] == "9":
        a+=1
    return a

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
        print(res)