
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
            dyndown[2] = (dyndown[2] + dyndown[2] + dyndown[1])%mod
            dynup[2] = (dynup[2] + dynup[2])%mod
            dynup[0] = (dynup[0] + dynup[0] + 1)%mod

        else:
            # dyndown[x+2] = (dynup[x] + dyndown[x+2])%mod
            dyndown[x+1] = (dyndown[x+1] + dyndown[x+1]+ dyndown[x])%mod
            # dyndown[x-1] if we add x and mex is x-1 then this is a dynup
            dynup[x-1] = (dynup[x-1] + dynup[x-1] + dyndown[x-1])%mod
            dynup[x+1] = (dynup[x+1] + dynup[x+1])%mod
    ans = 0
    for x in dynup:
        ans = (ans +x )%mod
    for x in dyndown:
        ans = (ans +x )%mod

    return ans


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
