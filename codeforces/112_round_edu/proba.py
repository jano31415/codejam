def solve(n):
    if n%6 == 0:
        return n//6 * 15
    if n <= 6:
        return 15
    if n <= 8:
        return 20
    if n <= 10:
        return 25
    if n % 6 in [3,4]:
        return (n//6-1) * 15 + 25
    elif n%6 in [1,2]:
        return (n // 6 - 1) * 15 + 20
    else:
        return (n // 6 + 1) * 15

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