import math
def solve(n, arr):
    first=0
    second=0
    for i in range(n):
        if n%2==1 and i == n//2:
            if arr[i] == i + 1:
                first += 1
            continue
        if arr[i] == i+1:
            first+=1
        if arr[i] == n-i:
            second+=1
    moves_first = n//2
    moves_second = n//2 - (n+1)%2
    if first > moves_second:
        return "First"
    if second > moves_first:
        return "Second"
    return "Tie"


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]
        res = solve(n, arr)
        print(res)
# import time
# a=time.time()
# n=10000
# solve(n=n, dep=[[]]+[set([i+2]) for i in range(n-1)]+[set()])
# b=time.time()
# print(b-a)