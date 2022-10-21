def solve(n, arr):

    arr.sort()
    start = 0
    cur = 0
    smaller_eq = [0]*(n+1)
    for i in range(n+1):
        while start < n and arr[start] <= i:
            cur+=1
            start+=1
        smaller_eq[i] = cur
    # print(smaller_eq)
    for k in reversed(range(n+1)):
        works=True
        for i,x in enumerate(smaller_eq[1:], start=1):
            if i == k+1:
                break
            if x-(k-1) < i:
                works=False
                break
        if works:
            return k
    return 0


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

