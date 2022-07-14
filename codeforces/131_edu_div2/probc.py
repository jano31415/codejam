import math
def solve(n,m,a):
    left = 0
    right = 2*m//n + 2
    counts = [0]*n
    for ax in a:
        counts[ax-1] += 1
    while left < right:
        middle = (left + right) // 2
        if check_smaller(counts, middle, m):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(counts, total_t, m):
    sum_done = 0
    for c in counts:
        if c >= total_t:
            sum_done += total_t
        else:
            sum_done += c + (total_t-c)//2
    if sum_done >= m:
        return False
    return True

def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = (left + right) // 2
        if check_smaller(array, middle, find_this_number):
            left = middle + 1
        else:
            right = middle
    return left
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        a = [int(x) for x in input().decode().strip().split()]

        res=solve(n,m,a)
        print(res)

