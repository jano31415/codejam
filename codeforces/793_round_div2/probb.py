import math
def solve(n,arr):
    X = 2**(int(math.log2(n))+1) - 1
    for i,a in enumerate(arr):
        if i != a:
            X = X&i
    return X
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]

        res=solve(n,arr)
        print(res)

