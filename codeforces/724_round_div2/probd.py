import math
def solve(arr):
    sorted = [arr[0]]
    # last = sorted[0]
    bigm =10**10
    # sol = []
    # count_small = 0

    for i,x in enumerate(arr):
        if i == 0:
            continue
        if i == 1:
            if sorted[0] == x:
                sorted.insert(0, -bigm)
                sorted.append(bigm)
            elif sorted[0] < x:
                sorted.append(x)
                sorted.append(bigm)
            else:
                sorted.insert(0,x)
                sorted.insert(0, -bigm)
            continue

        # index = binary_search_leftmost(sorted, x)
            if sorted[i-2] == x:
                sorted.insert(0, -bigm)
                sorted.insert(0, -bigm)
                # count_small += 2
            elif sorted[i-1] == x:
                sorted.insert(0, -bigm)
                sorted.append(bigm)

                # count_small+= 1
            elif (sorted[i-2] < x) and (sorted[i-1] > x):
                sorted.insert(0, -bigm)
                sorted.insert(i, x)
            elif (sorted[i-1] < x) and (sorted[i] > x):
                sorted.insert(i, x)
                sorted.append(bigm)

            elif sorted[i] == x:
                sorted.append(bigm)
                sorted.append(bigm)
                # pass # 2 +bigm
            else:
                return "NO"
        # if sorted[index] < x:
        #     sorted.insert(index+1, x)
        #     index = index+1
        # elif sorted[index] > x:
        #     sorted.insert(index, x)
        # else:
        #     if index+count_small < i:
        #         count_small += 1
        #
        # if index+count_small == i-1:
        #     count_small+=1
        # elif index+count_small != i:
        #     return "NO"
    return "YES"

from heapq import heapify, heappush, heappop
def solve_heap(arr):
    bigm = 10**10
    upper = []
    heapify(upper)
    lower = [-arr[0]]
    heapify(lower)
    for i,x in enumerate(arr):
        if i ==0:
            continue
        if len(lower) > len(upper):
            if x > -lower[0]:
                if len(upper) > 0:
                    if x > upper[0]:
                        return "NO"
                    elif x == upper[0]:
                        heappush(upper, bigm)
                        heappush(upper, bigm)
                        heappush(lower, -heappop(upper))
                        continue
                heappush(upper, x)
                heappush(upper, bigm)
                heappush(lower, -heappop(upper))
            elif x == -lower[0]:
                heappush(lower, -(-bigm))
                heappush(upper, bigm)
            else:
                tmp = -heappop(lower)
                if len(lower) != 0:
                    if -lower[0] > x:
                        return "NO"
                    elif -lower[0] == x:
                        heappush(lower, -(-bigm))
                        heappush(lower, -(-bigm))
                        heappush(upper, tmp)
                        continue
                heappush(lower, -x)
                heappush(lower, -(-bigm))
                heappush(lower, -tmp)
                heappush(upper, -heappop(lower))
        else:
            print("heap wrong size")
    return "YES"


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

def check_smaller(array, middle, find_this_number):
    # might be slightly different if this is not an array
    return array[middle] < find_this_number

def binary_search_rightmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = math.floor((left + right) / 2)
        if check_bigger(array, middle, find_this_number):
            right = middle
        else:
            left = middle + 1
    return right-1

def check_bigger(array, middle, find_this_number):
    # might be slightly different if this is not an array
    return array[middle] > find_this_number

if __name__ == "__main__":
    cache = {}
    T = int(input())
    for t in range(T):
        N = int(input())
        arr = [int(x) for x in input().split(" ")]
        res = solve_heap(arr)
        print(res, flush=True)

# import random
# N=10**5
# a = [random.randint(0,10**5) for _ in range(N)]
# import time
# time1=time.time()
# newl = []
# for x in a:
#     newl.insert(len(newl)//2, x)
# time2 = time.time()
# print(time2-time1)
#
# from heapq import heapify, heappush
# time1=time.time()
# newl = []
# heapify(newl)
# for x in a:
#     heappush(newl, x)
# time2 = time.time()
# print(time2-time1)

# def check_sol(sol, arr):
#     for i in range(len(sol)//2):
#         cur = sol[:2*i-1]
#         cur.sort()
#         if arr[i] != cur[i]:
#             return "NO"
#     return "YES"
#
# import random
# for i in range(100):
#     N=15
#     arr = [random.randint(-10,10) for x in range(N)]
#     res,sol = solve(arr)
#     if len(sol) != 2*len(arr)-1:
#         continue
#     correct = check_sol(sol,arr)
#     if res != correct:
#         print(arr)