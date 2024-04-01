def solve(n,k):
    if n == k:
        arr = [1]*n
    elif k == 1:
        arr = [1]*(n-1)+[2]
    else:
        return "-1"
    return " ".join([str(x) for x in arr])



import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]

        res = solve(n,k)
        print(res)