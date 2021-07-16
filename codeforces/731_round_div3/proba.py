def solve(a1,a2,b1,b2,f1,f2):

    dist = abs(a1 - b1) + abs(a2 - b2)
    if a1 == b1:
        if f1 == a1 and (f2 < max(a2,b2) and (f2 > min(a2,b2))):
            dist+=2
    elif a2 == b2:
        if f2 == a2 and (f1 < max(a1, b1) and (f1 > min(a1, b1))):
            dist+=2
    return dist
import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input()
        a1,a2 = [int(x) for x in input().decode().strip().split(" ")]
        b1,b2 = [int(x) for x in input().decode().strip().split(" ")]
        f1,f2 = [int(x) for x in input().decode().strip().split(" ")]

        res = solve(a1,a2,b1,b2,f1,f2)
        print(res)