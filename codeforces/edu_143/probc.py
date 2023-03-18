def solve(n,a,b):
    cumbi = [0]*(n+1)
    cumsum = 0
    countb = [0]*n
    rest = [0]*(n+1)
    tot=0
    for i,bi in enumerate(b):
        cumbi[i]=tot
        tot+=b[i]
    cumbi[n]=tot
    # cumbi[-1] = cumbi[n]+10**9
    diff = [0]*(n+2)
    for i,ai in enumerate(a):
        j = binary_search_leftmost(cumbi, ai, i)

        diff[i+1] += 1
        if cumbi[j]-cumbi[i] >= ai:
            diff[j] -= 1
            rest[j-1] += min(b[j-1], ai-(cumbi[j-1]-cumbi[i]))
        else:
            diff[j+1] -=1
            rest[j] += min(b[j-1], ai-(cumbi[j-1]-cumbi[i]))

    arr2 = [0]*(n+1)
    for i in range(len(arr2)):
        if i == 0:
            arr2[0] = diff[0]
        else:
            arr2[i] = diff[i] + arr2[i - 1]
    resb = [0]*n
    for i in range(n):
        resb[i] = arr2[i+1]*b[i] + rest[i]
    return " ".join([str(x) for x in resb])

import math
def binary_search_leftmost(array, find_this_number, left_start):
    left = left_start
    right = len(array)-1
    while left < right:
        middle = math.floor((left + right) / 2)
        if find_this_number > array[middle]-array[left_start]:
            left = middle + 1
        else:
            right = middle
    return left

def difference_array(arr2, l, r, v):
    # create a difference array
    diff = [arr2[0]] + [arr2[i] - arr2[i - 1] for i in range(1, len(arr2))]
    # update the range by adding the value for the first and then subtracting it
    # at the end of the range
    for i in range(len(l)):
        diff[l[i]] += v[i]
        diff[r[i]] -= v[i]

    # reconstruct the updated array
    for i in range(len(arr2)):
        if i == 0:
            arr2[0] = diff[0]
        else:
            arr2[i] = diff[i] + arr2[i - 1]
    return arr2

import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        ai = [int(x) for x in input().decode().strip().split()]
        bi = [int(x) for x in input().decode().strip().split()]

        res = solve(n,ai,bi)
        print(res)