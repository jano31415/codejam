def solve(a,b):

    mina = min(a,b)
    maxb = max(a,b)
    n = a+b
    min_sol = (maxb-mina)//2
    max_sol = n-min_sol

    if (a+b)%2 == 0:
        return [str(x) for x in list(range(min_sol, max_sol+1, 2))]
    else:
        return [str(x) for x in range(min_sol, max_sol+1, 1)]

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(a, b)
        # check(res)
        print(len(res))
        print(" ".join(res))
