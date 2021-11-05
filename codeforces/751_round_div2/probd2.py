import collections
from heapq import heapify, heappop, heappush
# initializing deque


def solve(n, a, b):
    a = [0]+a
    b = [0]+b
    dyn = [10*n]*(n+1)
    dyn[n] = 0
    pred = [-1]*(n+1)
    jumps = [-1]*(n+1)
    # bfs dist is 1
    seen = set([n])
    hot = [(n,0)]
    heapify(hot)
    while len(hot) > 0:
        current,dist = heappop(hot)
        if dyn[current] + 1 > dyn[0]:
            continue
        # print(f" current {current}")
        for j in range(a[current]+1):
            # print(f" j {j}")
            jump_up_pos = current-j
            fall_down = jump_up_pos + b[jump_up_pos]
            if dyn[fall_down] > dyn[current] + 1:
                if fall_down not in seen:
                    heappush(hot, (fall_down, dyn[current] + 1))
                    seen.add(fall_down)
                dyn[fall_down] = dyn[current] + 1
                pred[fall_down] = current
                jumps[fall_down] = jump_up_pos


    if dyn[0] == 10*n:
        print(-1)
        return

    res = []
    point = 0
    while point != n:
        if pred[point] == -1:
            print("-1")
            return
        res.append(str(jumps[point]))
        point=pred[point]
    res = res[::-1]
    print(dyn[0])
    print(" ".join(res))




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    n = int(input().decode().strip())
    a =[int(x) for x in input().decode().strip().split(" ")]
    b =[int(x) for x in input().decode().strip().split(" ")]
    res=solve(n, a, b)

