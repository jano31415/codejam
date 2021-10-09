def solve(n,k):
    mod = 10**9 + 7

    a="{0:#b}".format(k)
    a = a[::-1]
    pow =1
    tot = 0
    for x in a:
        if x =="1":
            tot = (tot + pow) %mod
        pow = pow*n
    return tot



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split(" ")]

        res = solve(n,k)
        # check(res)
        print(res)
