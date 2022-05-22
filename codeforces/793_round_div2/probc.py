import math
def solve2(n,arr):
    l =[]
    lrev = []
    arr.sort()
    for i in range(n):
        if i %2 ==0:
            l.append(arr[i])
        else:
            lrev.append(arr[i])
    cur = 0
    resl =0
    for x in l:
        if cur < x:
            resl +=1
        cur = x
    cur = 0
    reslrev = 0
    for x in lrev:
        if cur < x:
            reslrev +=1
        cur = x
    if resl != reslrev:
        if set(l) != set(lrev):
            return min(resl, reslrev) + 1
    return min(resl, reslrev)

def solve(n,arr):
    keys = set(arr)
    counter = {k:0 for k in keys}
    for a in arr:
        counter[a] += 1

    res = 0
    round = False
    for k in counter:
        if counter[k] >= 2:
            res+=2
        if counter[k] == 1:
            res+=1
            round=True

    if round:
        res = res + res%2
    return res//2

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

