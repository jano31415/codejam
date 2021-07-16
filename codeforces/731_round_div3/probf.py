
import math
class RMQ:
    def __init__(self, arr, min_max):
        self.cache = [arr]
        self.func = min_max
        self.precompute(arr, self.func)

    def precompute(self, arr, min_max):

        max_log = int(math.log2(len(arr)))
        for i in range(1, max_log + 1):
            new_row = []
            for j in range(0, len(arr) - 2 ** i + 1):
                new_row.append(min_max(self.cache[i - 1][j],
                                       self.cache[i - 1][j + 2 ** (i - 1)]))
            self.cache.append(new_row)

    # should be equal to min(arr[l:r]) care l == r, plus minus 1 error
    def query(self, l, r):
        if l == r:
            return self.cache[0][l]
        if l > r:
            return self.func(self.query(l,n), self.query(0,r))
        log_val = int(math.log2(r - l))
        return self.func(self.cache[log_val][l],
                         self.cache[log_val][r - 2 ** log_val])



def binary_search_leftmost(rmq, min_all, n, cur):
    left = 0
    right = n-1
    while left < right:
        middle = (left + right) // 2
        if check_smaller(rmq, middle, min_all, cur):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(rmq, middle, min_all, cur):
    # might be slightly different if this is not an array
    if (cur + middle) % n + 1 == cur:
        res1 = min_all
    else:
        res1 = rmq.query(cur, (cur + middle) % n + 1)
    if res1 == min_all:
        return False
    return True

def solve(n,seq):
    rmq = RMQ(seq, math.gcd)
    min_all = rmq.query(0,n)
    max_op = 0
    cur = 0

    while cur < n:
        if seq[cur] == min_all:
            cur+=1
            continue
        mid = binary_search_leftmost(rmq, min_all, n, cur)
        if mid > max_op:
            max_op = mid
        cur = cur+1
    return max_op


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        seq=[int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,seq)
        print(res)