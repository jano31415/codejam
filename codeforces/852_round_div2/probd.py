def solve(arr1, arr2, n):
    map1 = [0]*(n+1)
    map2 = [0]*(n+1)
    for i in range(n):
        map1[arr1[i]-1] = i
        map2[arr2[i]-1] = i

    left = min(map1[0], map2[0])
    right= max(map1[0], map2[0])
    tot = (left*(left+1))//2
    tmp = n-right-1
    tot += (tmp*(tmp+1))//2
    if left+1 <= right-1:
        tmp+= (right-1 - (left+1))
        tot += (tmp*(tmp+1))//2

    for mex in range(n):
        left = min([map1[mex], map2[mex], left])
        right = max([map1[mex], map2[mex], right])
        l = [x for x in [map1[mex+1], map2[mex+1]] if x <= right]
        lnext = 0 if len(l)==0 else max(l)+1
        if left < lnext < right:
            continue
        r = [x for x in [map1[mex+1], map2[mex+1]] if x >= left]
        rnext = n-1 if len(r)==0 else min(r)-1
        if left < rnext < right:
            continue
        print((left-lnext+1)* (rnext-right+1))
        tot += (left-lnext+1)* (rnext-right+1)
    if left != 0 or right != n-1:
        tot+=1
    return tot

import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n = int(input().decode().strip())
    arr1 = [int(x) for x in input().decode().strip().split()]
    arr2 = [int(x) for x in input().decode().strip().split()]

    res = solve(arr1, arr2, n)
    print(res)