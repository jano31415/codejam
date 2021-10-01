def solve(n):
    for i in range(n):
        print("(" * (i+1) +")" +"("* (n-i-1) + ")"*(n-1))

import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for i in range(T):
        n = int(input().decode().strip())

        a = solve(n)
