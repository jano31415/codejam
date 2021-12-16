def solve(n, h, attacks):
    diffs = [0]*n
    for i,a in enumerate(attacks):
        if i == (n-1):
            continue
        diffs[i] = attacks[i+1] - attacks[i]
    diffs[-1] = h
    k=binary_search_leftmost(diffs, h)
    return k

def binary_search_leftmost(diffs, h):
    left = 1
    right = h
    while left < right:
        middle = (left + right) // 2
        if check_smaller(diffs, middle, h):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(diffs, middle, h):
    cum = 0
    for d in diffs:
        cum += min(d, middle)
    return cum < h




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,h =[int(x) for x in input().decode().strip().split(" ")]
        attacks = [int(x) for x in input().decode().strip().split(" ")]
        assert len(attacks) == n
        res=solve(n, h, attacks)
        print(res, flush=True)
