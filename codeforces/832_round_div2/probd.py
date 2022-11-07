import random
from sys import stdout


# def print(msg, flush=None):
#     stdout.write(msg + '\n')
#     stdout.flush()

class Tree:
    def __init__(self, n):
        self.tree = [0] * (2 * n+2)
        self.n=n

    # function to build the tree
    def build(self, arr):

        # insert leaf nodes in tree
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]

            # build the tree by calculating parents
        for i in range(self.n-1, 0, -1):
            # print(f"parent {i}: {2*i} {2*i+1}")
            self.tree[i] = self.tree[2*i] ^ self.tree[2*i+1]


    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n

        while l < r:

            if l%2 == 1:
                res ^= self.tree[l]
                l += 1

            if r %2 == 1:
                r -= 1
                res ^= self.tree[r]

            l //= 2
            r //= 2

        return res

def solve(n,arr, queries):
    # import math
    # log = int(math.log2(n))
    next=n
    # if n != 2**log:
    #     next = 2**(log+1)

    seg = Tree(next)
    seg.build(arr)
    prefix = [0]*(n+1)
    cur =0
    for i,x in enumerate(arr):
        prefix[i]=cur
        cur+=x
    prefix[-1]=cur
    # seg0 = Tree0(next)
    # seg0.build(arr)
    for l,r in queries:
        l0=l-1
        r0=r-1
        if prefix[r]==prefix[l0]:
            print(0)
        elif l == r:
            print(-1)
        elif (r-l0)%2 == 1:
            if seg.query(l0, r) == 0:
                print(1)
            else:
                print(-1)
        elif arr[l0] == 0 or arr[r0] == 0:
                if seg.query(l0, r) == 0:
                    print(1)
                else:
                    print(-1)
        else:
            if seg.query(l0, r) == 0:
                splitfound=False
                cur =0
                for i in range(l0,r):
                    cur^=arr[i]
                    if cur == 0 and (i-l0+1)%2==1:
                        splitfound=True
                        break

                # for i in range(l0+3,r0,2):
                #
                #     if (i-l0)%2==1:
                #         if seg.query(l0, i) == 0:
                #             splitfound=True
                #             break
                if splitfound:
                    print(2)
                else:
                    print(-1)
            else:
                print(-1)


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,q = [int(x) for x in input().decode().strip().split()]
    arr = [int(x) for x in input().decode().strip().split()]
    queries = [None]*q
    for i in range(q):
        l, r = [int(x) for x in input().decode().strip().split()]
        queries[i] = (l,r)
    solve(n,arr,queries)

# N=200000
# maxn=10**30
# import random
# import time
# arr=[random.randint(0,maxn) for _ in range(N)]
# queries=[random.randint(0,N-1) for _ in range(N)]
# queries=[(l,min(N,l+random.randint(0,N//2))) for _ in range(N)]
# a=time.time()
# solve(N,arr,queries)
# print(str(time.time()-a))