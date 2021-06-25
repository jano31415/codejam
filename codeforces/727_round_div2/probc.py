def solve(n, k,x ,numbers):
    numbers.sort()
    grp_diff = []
    for i,a in enumerate(numbers):
        if i ==0:
            continue
        if numbers[i] - numbers[i-1] > x:
            grp_diff.append(numbers[i] - numbers[i-1])
    grp_diff.sort()
    k_left = k
    for i,diff in enumerate(grp_diff):
        new_needed = diff//x
        if diff == x * new_needed:
            new_needed -= 1
        if k_left >= new_needed:
            k_left -= new_needed
        else:
            return len(grp_diff) - i + 1
    return 1

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,k,x = [int(x) for x in input().decode().strip().split(" ")]
    numbers = [int(x) for x in input().decode().strip().split(" ")]
    res = solve(n,k,x,numbers)
    print(res)