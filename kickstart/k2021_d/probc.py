import math


def solve(n,m,intervals,students):
    intervals.sort(key=lambda x:x[0])
    assignemnts=[]
    for s in students:
        mid = binary_search_leftmost(intervals,s)
        l,r = intervals[mid]
        if s >= l and s <=r:
            remove_s = s
        elif s >= r:
            remove_s = r
            if mid < len(intervals)-1:
                if abs(intervals[mid+1][0] - s) < abs(r-s):
                    l,r = intervals[mid+1]
                    mid = mid+1
                    remove_s = l
        elif s<=l:
            remove_s = l
            if mid > 0:
                if abs(intervals[mid-1][1] - s) <= abs(l-s):
                    l,r = intervals[mid-1]
                    mid = mid-1
                    remove_s = r

        assignemnts.append(remove_s)
        if remove_s <= l:
            if l == r:
                intervals.pop(mid)
            else:
                intervals[mid] = (l+1, r)
        elif remove_s >= r:
            if l == r:
                intervals.pop(mid)
            else:
                intervals[mid] = (l, r-1)
        else:
            intervals[mid] = (l, remove_s-1)
            intervals = intervals[:mid+1] +[(remove_s+1,r)] + intervals[mid+1:]
    return [str(x) for x in assignemnts]

def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = math.floor((left + right) / 2)
        if check_smaller(array, middle, find_this_number):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(array, middle, find_this_number):
    # might be slightly different if this is not an array
    if array[middle][0] > find_this_number:
        return False
    # if array[middle][1] < find_this_number:
    #     return True
    return array[middle][0] < find_this_number

if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input())
    for t in range(1,T+1):
        n,m = [int(x) for x in input().split(" ")]
        intervals = []
        for _ in range(n):
            row = [int(x) for x in input().split(" ")]
            intervals.append(row)
        students = [int(x) for x in input().split(" ")]
        res = solve(n,m,intervals,students)
        print(f"Case #{t}: {' '.join(res)}", flush=True)

# import random
# N=100000
# l=[random.randint(0,10**8) for _ in range(N)]
# l =[(a,a+random.randint(0,100)) for a in l]
# s =[random.randint(0,10**8) for s in range(N)]
# import time
# a=time.time()
# res = solve(100,100, l,s)
# b=time.time()
# print(b-a)
# print(res)