def solve(n, di):
    tot = max(di)
    # di.pop(0)
    # if len(di) == 0:
    #     return tot
    di.sort()
    right_sum = sum(di)
    for i,d in enumerate(di):
        right_sum -= d
        # tot += left_sum - i*d
        tot += (n-i-1)*d - right_sum
        # left_sum+=d

    return tot
import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    amounts = []
    for i in range(T):
        n = int(input().decode().strip())
        di = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,di)
        print(res)