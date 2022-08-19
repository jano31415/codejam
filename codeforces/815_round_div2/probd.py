def solve(n, arr):
    dyn = [1] * len(arr)
    for lasti, x in enumerate(dyn):
        # if lasti > 1024:
        #     break
        endj = min(len(arr), lasti - lasti%256 + 256)
        arrlasti = arr[lasti]
        dynlasti = dyn[lasti]
        dynlasti1 = dyn[lasti]+1
        for j in range(lasti+1, endj):
            # if j >= len(dyn):
            #     continue
            # if j >= len(arr):
            #     continue
            if arrlasti ^ j < arr[j] ^ lasti:
                if dyn[j] <= dynlasti:
                    dyn[j] = dynlasti1
    return max(dyn)





import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())

    for t in range(T):
        n = int(input().decode().strip())

        arr = [int(x) for x in input().decode().strip().split()]
        res=solve(n, arr)
        print(res)

# for i in range(1024, 1200):
#     for j in range()
# from random import randint
# import time
# n=3*10**5
# arr=[randint(0,200) for x in range(n)]
# a=time.time()
# solve(n,arr)
# b=time.time()
# print(b-a)