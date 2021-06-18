import math
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

def binary_search_rightmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = (left + right) // 2
        if array[middle] > find_this_number:#check_smaller(array, middle, find_this_number):
            right = middle
        else:
            left = middle + 1

    return right# - 1


def check_smaller(array, middle, find_this_number):
    # might be slightly different if this is not an array
    return array[middle] < find_this_number


def solve(n,l,r,stones):
    stones = [s for s in stones if s<r]
    stones.sort()
    tot = 0
    pairs = []
    # for s in stones:
    while len(stones) > 1:
        s = stones.pop()
        # s=stones[0]
        # if s >= r:
        #     return tot
        index_min = binary_search_leftmost(stones, max(0,l-s))
        # index_min = 0
        index_max = binary_search_rightmost(stones, r-s)
        # index_max=0
        tot += (index_max - index_min)
        # if stones[index_min] + s >= l and stones[index_min] + s <= r:
        #     tot+=1
        # if (index_max == index_min) or (r-s == stones[index_max]):
        #     if stones[index_max] + s >= l and stones[index_max] + s <= r:
        #         tot += stones.count(stones[index_max:])
        #     # print(1)
        #     pass
        # else:
        if stones[index_max] + s >= l and stones[index_max] + s <= r:
            tot += 1  # stones.count(stones[index_max])
        # stones = stones[:index_max]
        # if index_max < 0.9*len(stones):
        #     stones = [a for a in stones if a<r-s]
    return tot

def solve_slow(n,l,r, stones):
    tot=0
    for i,x in enumerate(stones):
        for j in range(i+1,n):
            y = stones[j]
            if x+y >= l and x+y <= r:
                tot+=1
    return tot

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,l,r = [int(x) for x in input().decode().strip().split(" ")]
        stones = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,l,r,stones)
        print(res)

# import random
# import time
# for i in range(1):
#     n=2*10**5
#     stones = [random.randint(0,100) for _ in range(n)]
#     stones_org = stones[:]
#     l=int(3*min(stones))
#     r= int(1.2*max(stones))
#     print("random")
#     res1=3
#     # res1=solve_slow(n,l,r,stones)
#
#     print(res1)
#     time1 = time.time()
#     res2=solve(n,l,r,stones)
#     print(res2)
#     # if res1!=res2:
#     #     print(stones_org)
#     #     solve(n,l,r,stones_org)
#     #     raise ValueError()
#     print("random end")
# time2= time.time()
# print(time2-time1)