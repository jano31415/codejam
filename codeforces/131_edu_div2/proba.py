import math
def solve(l):
    if sum(l)==0:
        return 0
    elif sum(l) == 4:
        return 2
    return 1


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        a1,a2 = [int(x) for x in input().decode().strip().split()]
        a3,a4 = [int(x) for x in input().decode().strip().split()]

        res=solve([a1,a2,a3,a4])
        print(res)

