def solve(N, stones):
    min_val = 10**5
    min_index = 0
    max_index = 0
    max_val = -1
    for i,x in enumerate(stones):
        if x <= min_val:
            min_val = x
            min_index = i
        if x >= max_val:
            max_val = x
            max_index = i
    left_right = N - (abs(min_index-max_index)-1)
    left_both = max(min_index, max_index) + 1
    right_both = N-min(min_index, max_index)
    return min(left_right,left_both , right_both)


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        N = int(input().decode().strip())
        stones = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(N, stones)
        print(res)