import math
def solve(n,a,b):
    return a[sum(b)%n]
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a = [int(x) for x in input().decode().strip().split()]
        m = int(input().decode().strip())
        b = [int(x) for x in input().decode().strip().split()]
        res1= solve(n,a,b)
        print(res1)


