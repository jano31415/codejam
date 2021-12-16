
def solve(n, seq):
    mod = 998244353
    dynup = [0]*(n+3)
    dyndown = [0]*(n+3)

    # dyn[0] = 1
    for i,x in enumerate(seq):
        if x == 0:
            # dyndown[2] = (dyndown[2] + dynup[0])%mod
            dyndown[1] = (2*dyndown[1] + 1)%mod
            dynup[1] = (dynup[1] + dynup[1])%mod
        elif x == 1:
            # dyndown[3] = (dyndown[3] + dynup[1])%mod
            dyndown[2] = (dyndown[2] + dyndown[1])%mod
            dynup[2] = (dynup[2] + dynup[2])%mod
            dynup[0] = (dynup[0] + dynup[0] + 1)%mod

        else:
            # dyndown[x+2] = (dynup[x] + dyndown[x+2])%mod
            dyndown[x+1] = (dyndown[x] + dyndown[x+1])%mod
            # dyndown[x-1] if we add x and mex is x-1 then this is a dynup
            dynup[x-1] = (dynup[x-1] + dynup[x-1] + dyndown[x-1])%mod
            dynup[x+1] = (dynup[x+1] + dynup[x+1])%mod


    return sum(dynup) + sum(dyndown)




def binary_search_leftmost(diffs, h):
    left = 1
    right = h
    while left < right:
        middle = (left + right) // 2
        if check_smaller(diffs, middle, h):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(diffs, middle, h):
    cum = 0
    for d in diffs:
        cum += min(d, middle)
    return cum < h




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        seq = [int(x) for x in input().decode().strip().split(" ")]
        assert len(seq) == n
        res=solve(n, seq)
        print(res, flush=True)
