import math
def solve(n):
    mod = 10**9+7
    tot = 2*n % mod
    biggest_div = 2
    fact = biggest_div
    while fact <= n:
        tot = (tot + n // fact) % mod
        biggest_div = biggest_div + 1
        new_fac = biggest_div // math.gcd(fact, biggest_div)
        fact = fact * (new_fac)
    return tot


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res = solve(n)
        print(res)