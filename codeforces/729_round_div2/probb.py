def solve(a,b,n):
    if n % b == 1:
        return "Yes"
    tmp = 1
    if a == 1:
        if (n - tmp) % b == 0:
            return "Yes"
        else:
            return "No"
    while tmp <= n:
        if (n - tmp) % b == 0:
            return "Yes"
        tmp = tmp*a
    return "No"

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,a,b = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(a,b,n)
        print(res)