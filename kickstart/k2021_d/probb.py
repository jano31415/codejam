from heapq import heapify, heappush, heappop
def solve(n, l,C):
    l.sort(key=lambda x:-x[0])
    first_close = []
    heapify(first_close)
    nr_interior = (n+1)*[0]
    last = l[-1][0]
    cur= 0
    while len(l) > 0 or len(first_close)>0:
        if len(first_close) > 0 and len(l)>0:
            new_point = min(l[-1][0], first_close[0])
        elif len(l) > 0:
            new_point = l[-1][0]
        else:
            new_point = first_close[0]

        if new_point-1 > last:
            nr_interior[cur] += new_point-1 - last
            last = new_point-1
        while len(first_close)!= 0 and first_close[0] == new_point:
            heappop(first_close)
            cur-=1

        nr_interior[cur] += new_point - last
        last = new_point
        while len(l)!=0 and l[-1][0] == new_point:
            open,close = l.pop()
            cur+=1
            heappush(first_close, close)


    tot = 0
    for i in reversed(range(n+1)):
        if nr_interior[i] < C:
            tot += nr_interior[i] * i
            C = C - nr_interior[i]
        else:
            tot += C * i
            C= 0
            return tot + n
    return tot + n
import io
import os
if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input())
    for t in range(1,T+1):
        n, c = [int(x) for x in input().split(" ")]
        l=[]
        for i in range(n):
            a,b = [int(x) for x in input().split(" ")]
            l.append((a,b))
        res = solve(n,l,c)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

import time
import random
N=100000
l = [random.randint(0,10000) for x in range(N)]
l = [(a, a+random.randint(0,500)) for a in l]

a =time.time()
solve(len(l), l, 10**10)
b=time.time()
print(b-a)
