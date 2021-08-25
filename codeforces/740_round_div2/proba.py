def solve(arr,n):
    max_sol = 0
    for i,x in enumerate(arr):
        sol = abs(x-(i+1))
        if sol > max_sol:
            max_sol = sol
    return max_sol

def solve_dumb(arr,n):
    if check(arr):
        return 0
    for i in range(n):
        for j in range(n):
            index = 2*j + i%2
            if index < n-1:
                # print(2*j + i%2)
                f(arr, 2*j + i%2)
        # print(arr)
        if check(arr):
            return (i+1)
    return n

def check(arr):
    for i,x in enumerate(arr):
        if (i+1) !=x:
            return False
    return True

def f(arr,i):
    if arr[i] > arr[i+1]:
        tmp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = tmp
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split(" ")]
        res = solve_dumb(arr, n)
        # check(res)
        print(res)
