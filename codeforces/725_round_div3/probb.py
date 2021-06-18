def solve(N, stones):
    tot = sum(stones)
    if tot % N != 0:
        return -1
    if len(set(stones)) == 1:
        return 0
    stones.sort(reverse=True)
    avg = tot//N
    needed =0
    # for x in reversed(stones):
    #     needed +=
    cumsum = 0
    for i,x in enumerate(stones):
        if x <= avg:
            return i
        # cumsum += x
        # if cumsum - (i+1)*avg >= (N-i-1)*avg - (tot-cumsum):
        #     return i
    return N
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