import math
def solve(n, arr):
    arr_sorted = sorted(arr)
    if arr == arr_sorted:
        return "NO"
    return "YES"

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split(" ")]
        res1 = solve(n, arr)
        print(res1)
        # print("\n")