import math
def solve(n,c,q, copies, queries):
    lengths = [0, n]
    for l,r in copies:
        new_length = lengths[-1] + r-l+1
        lengths.append(new_length)
    lengths[-1] += 1
    for q in queries:
        qbefore = q
        while qbefore > n:
            pos = binary_search_leftmost(lengths, qbefore)
            qbefore = copies[pos-2][0]-1 + qbefore-lengths[pos-1]
        print(s[qbefore-1])
#mark 4 0-3
#markmark 8 0-7
#markmarkmar 11 0-10
#markmarkmarrkmark 17 0-16

def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = (left + right) // 2
        if array[middle] < find_this_number:  # check_smaller(array, middle, find_this_number):
            left = middle+1
        else:
            right = middle
    return left

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,c,q = [int(x) for x in input().decode().strip().split()]
        s = input().decode().strip()
        copies = []
        for i in range(c):
            l,r = [int(x) for x in input().decode().strip().split()]
            copies.append((l,r))
        queries = []
        for i in range(q):
            queries.append(int(input().decode().strip()))
        res=solve(n,c,q, copies, queries)

