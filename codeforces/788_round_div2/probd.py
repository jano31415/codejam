import math
def get_max_k():
    max_lines=40000
    dp={}
    dp[(0,0,0)] = 0
    dp[(0,0,1)] = 0
    dp[(0,1,0)] = 0
    dp[(1,0,0)] = 0
    dp[(1,0,1)] = 2
    dp[(1,1,0)] = 2
    dp[(0,1,1)] = 2
    dp[(1,1,1)] = 4

    max_k = [0]
    margin=2
    # three types of lines
    for k in range(1, max_lines):
        max_k.append(0)
        minx = max(0, k//3 - margin)
        for x1 in range(minx, k//3 +margin):
            for x2 in range(minx, k//3 + margin):
                x3 = k - x1 - x2
                # if x3 < 0:
                #     continue
                try:
                    if max([x1,x2,x3]) == x3:
                        dp[(x1,x2,x3)] = dp[(x1,x2,x3-1)] + 2*x1 + 2*x2
                    elif max([x1,x2,x3]) == x2:
                        dp[(x1,x2,x3)] = dp[(x1,x2-1,x3)] + 2*x1 + 2*x3
                    else:
                        dp[(x1,x2,x3)] = dp[(x1-1,x2,x3)] + 2*x2 + 2*x3
                    res = dp[(x1,x2,x3)]
                    if res > max_k[k]:
                        max_k[k] = res
                    if max_k[k] > 10**9:
                        # print(f"use {k}")
                        return max_k
                except KeyError:
                    continue
    return max_k

def solve(n, max_k):
    return binary_search_rightmost(max_k, n)

def binary_search_rightmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = (left + right) // 2
        if array[middle] >= find_this_number:#check_smaller(array, middle, find_this_number):
            right = middle
        else:
            left = middle + 1

    return right# - 1

def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = (left + right) // 2
        if array[middle] < find_this_number:#check_smaller(array, middle, find_this_number):
            left = middle + 1
        else:
            right = middle
    return left

def check_bigger(array, middle, find_this_number):
    # might be slightly different if this is not an array
    return array[middle] > find_this_number



import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    max_k = get_max_k()

    for t in range(T):
        n = int(input().decode().strip())
        res=solve(n, max_k)
        print(res)
# print(time.time() -a)
