import math
def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = math.floor((left + right) / 2)
        if check_smaller(array, middle, find_this_number):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(array, middle, find_this_number):
    # might be slightly different if this is not an array
    return array[middle] <= find_this_number


def solve(xstreets, ystreets, peoples):
    y_between = get_y_between(peoples, ystreets, False)

    x_between = get_y_between(peoples, xstreets, True)

    total = 0
    for s in y_between:
        interval = y_between[s]
        count = interval["count"]
        for xs in interval:
            if xs == "count":
                continue
            total += interval[xs] * (count - interval[xs])
            count -= interval[xs]

    for s in x_between:
        interval = x_between[s]
        count = interval["count"]
        for xs in interval:
            if xs == "count":
                continue
            # if count < interval[xs]:
            #     print("wron")
            total += interval[xs] * (count - interval[xs])
            count -= interval[xs]

    return total


def get_y_between(peoples, ystreets, swap):
    y_between = {}
    for px, py in peoples:
        if swap:
            tmp = px
            px = py
            py = tmp
        index = binary_search_leftmost(ystreets, py)
        if ystreets[index] != py and ystreets[max(index - 1, 0)] != py:
            if ystreets[index] not in y_between:
                y_between[ystreets[index]] = {"count": 0}
            tmp = y_between[ystreets[index]]
            tmp["count"] += 1
            if px not in tmp:
                tmp[px] = 0
            tmp[px] += 1
    return y_between


import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m,k = [int(x) for x in input().decode().strip().split(" ")]
        xstreets = [int(x) for x in input().decode().strip().split(" ")]
        assert len(xstreets) == n
        ystreets = [int(x) for x in input().decode().strip().split(" ")]
        assert len(ystreets) == m
        peoples = []
        for _ in range(k):
            px,py = [int(x) for x in input().decode().strip().split(" ")]
            peoples.append((px,py))
        res = solve(xstreets, ystreets, peoples)
        print(res)