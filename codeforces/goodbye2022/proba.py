def solve(n,m, arr, brr):
    b = sum(brr)
    arr.sort()
    for b in brr:
        mina=10**9
        mini=0
        for i,ai in enumerate(arr):
            if ai < mina:
                mina=ai
                mini=i
        arr[mini] = b
    return sum(arr)


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        arr = [int(x) for x in input().decode().strip().split()]
        brr = [int(x) for x in input().decode().strip().split()]

        res=solve(n,m, arr, brr)
        print(res)

