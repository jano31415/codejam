import math
from heapq import heapify,heappush,heappop


def solve(n, k, mines):
    if k==0:
        times = [x[2] for x in mines]
        return solve0(times)
    else:
        # this works only for k=1
        # k can be up to 10**9 which makes this infeasible
        return solve1(n,mines)

def solve0(times):

    times.sort(reverse=True)
    for i in range(len(times)):
        if times[i] < i:
            return i-1
    return len(times)-1

def solve1(n, mines):
    mines_locations = {(mx,my):t for mx,my,t in mines}
    mines_left = set(mines_locations.keys())
    components = []
    while len(mines_left) > 0:
        start_mine = mines_left.pop()
        #bfs
        q = [start_mine]
        seen = set(q)
        while len(q) > 0:
            cur = q.pop()
            try:
                mines_left.remove(cur)
            except Exception:
                pass
            for x,y in [(-1,0), (1,0), (0,-1), (0,1)]:
                next_node = (cur[0]+x, cur[1]+y)
                if next_node in mines_locations:
                    if next_node not in seen:
                        q.append(next_node)
                        seen.add(next_node)
        components.append(seen)
    comp_time = [min([mines_locations[x] for x in comp]) for comp in components]
    return solve0(comp_time)


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input().decode().strip()
        n,k = [int(x) for x in input().decode().strip().split(" ")]
        mines =[]
        for i in range(n):
            x, y, t = [int(x) for x in input().decode().strip().split(" ")]
            mines.append((x,y,t))
        res=solve(n,k, mines)
        print(res, flush=True)