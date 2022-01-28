import math
def solve(n,k, arr):
    arr_sorted = sorted(arr)
    minyx = 10**10
    best_xy = set()
    min_in_elements = k + math.ceil((n-k)/2)
    for i in range(n):
        x=arr_sorted[i]
        yi = i+min_in_elements-1
        if yi >= n:
            break
        y=arr_sorted[yi]
        if (y-x) < minyx:
            best_xy = set([(x,y)])
            minyx = y-x
        elif (y-x) == minyx:
            if (x,y) not in best_xy:
                best_xy.add((x,y))
    x,y = best_xy.pop()
    start = 0
    count_cur = 0
    count_in = 0
    split=[]
    for i,cur in enumerate(arr):
        if len(split) == k-1:
            split.append((start+1,n))
            break
        count_cur += 1
        if x <= cur and cur <= y:
            count_in+=1
        if count_in > (count_cur-count_in):
            split.append((start+1,i+1))
            start=i+1
            count_in=0
            count_cur=0
    return (x, y), split



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]
        arr = [int(x) for x in input().decode().strip().split()]
        res1,reslist = solve(n, k, arr)
        print(f"{res1[0]} {res1[1]}")
        for a,b in reslist:
            print(f"{a} {b}")
        # print("\n")