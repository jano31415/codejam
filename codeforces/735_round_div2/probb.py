def solve(n,k,arr):
    best = (1)*(2) - k * (arr[0] | arr[1])
    if n < 500:
        for i in range(n):
            for j in range(i+1,n):
                or_aij = arr[i] | arr[j]
                new = (i+1)*(j+1) - k * or_aij
                if new > best:
                    best = new
    else:
        for i in reversed(range(n-100, n)):
            for j in range(i-100, i):
                or_aij = arr[i] | arr[j]
                new = (i+1)*(j+1) - k * or_aij
                if new > best:
                    best = new
    return best
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split(" ")]
        arr = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,k,arr)
        print(res)