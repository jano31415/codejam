def solve(a,b):
    if b < a:
        tmp = a
        a = b
        b = tmp
    # obda a < = b
    diff = b - a
    if diff == 0:
        return f"{0} {0}"
    # if a == 0:
    # if b % diff == 0:
    #     return f"{diff} {0}"
    return f"{diff} {min(diff - b%diff, b%diff)}"


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(a,b)
        print(res)