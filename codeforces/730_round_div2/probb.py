def solve(n,cars):
    tot = sum(cars)
    # div = tot//n
    mod_div = tot % n
    return mod_div * (n-mod_div)


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        cars = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n, cars)
        print(res)