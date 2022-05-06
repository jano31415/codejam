import math
def solve(n,arr):
    count_neg = 0
    for x in arr:
        if x < 0:
            count_neg += 1
    last = arr[0]
    if count_neg >= 1:
        last = - abs(last)
    for i, x in enumerate(arr[1:], 1):
        if i < count_neg:
            x = -abs(x)
        else:
            x = abs(x)
        if x < last:
            return "NO"
        last = x
    return "YES"


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

