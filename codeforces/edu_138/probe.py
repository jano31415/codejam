def solve(n,m, grid):
    graph = {}
    forbidden = set()
    for ri,row in enumerate(grid):
        for ci,val in enumerate(row):
            rl = ri - 1
            rr = ri + 1
            cl = ci - 1
            cr = ci + 1
            neighbours = [(rl, ci), (rr, ci), (ri, cl), (ri, cr)]
            neighbours = [x for x in neighbours if
                          x[0] >= 0 and x[0] < n and x[1] >= 0 and x[1] < m]

            if any([grid[rn][cn] == "#" for rn,cn in neighbours if (rn,cn)!=(ri,ci)]):
                forbidden.add((ri,ci))
            else:
                graph[(ri, ci)] = []

    for ri,ci in graph:
        rl = ri-1
        rr = ri+1
        cl = ci-1
        cr = ci+1
        neighbours = [(rl,cl), (rl,cr), (rr,cl), (rr,cr)]
        neighbours = [x for x in neighbours if x[0]>=0 and x[0] < n and x[1]>=0 and x[1]<m]
        for rn, cn in neighbours:
            if (rn,cn) in forbidden:
                continue
            graph[(rn, cn)].append((ri, ci))
            graph[(ri, ci)].append((rn, cn))

    # bfs?
    open={}
    maxn = n + 500

    # for i in range(1, maxn+2):
    #     open[i] = set()
    from collections import deque
    start_nodes = [x for x in graph if x[1]==m-1]
    open[0] = deque([x for x in start_nodes if grid[x[0]][x[1]] == "#"])
    open[1] = deque([x for x in start_nodes if grid[x[0]][x[1]] == "."])
    seen = set()
    tot = 0
    walkback = {}
    while tot <= maxn:
        openl = open[tot]
        if tot+1 not in open:
            open[tot+1] = deque()
        while len(openl) > 0:

            cur = openl.pop()
            if cur in seen:
                continue
            if cur[1] == 0:
                # print(f"tot {tot}")
                return "YES", get_res_grid(cur,walkback,grid)
            for x in graph[cur]:
                if x not in seen:
                    tot_dist = tot
                    if grid[x[0]][x[1]] == ".":
                        tot_dist= tot+1
                    # open[tot+dist].add(x)
                    # open[tot_dist].append(x)
                    if x not in walkback:
                        walkback[x] = (cur, tot_dist)
                        open[tot_dist].append(x)

                    elif walkback[x][1] > tot_dist:
                        # walkback[x] = (cur, tot_dist)
                        open[tot_dist].append(x)

            seen.add(cur)
        tot += 1
    return "NO", None

def get_res_grid(cur,walkback, grid):
    while True:
        r,c = cur
        grid[r][c] = "#"
        cur,_ = walkback.get(cur, (0, m))
        if cur[1] == m-1:
            r, c = cur
            grid[r][c] = "#"
            return grid

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        grid = [None]*n
        for ri in range(n):
            row = list(input().decode().strip())
            grid[ri] = row

        res1,res2=solve(n,m, grid)
        print(res1)
        if res1 == "YES":
            for row in res2:
                print("".join(row))


import time
import random
for thresh in [0,0.1,0.3,0.5,0.7,0.9, 1]:
    thresh=0
    print(thresh)
    n=400
    m=1000
    grid=[["#" if random.random() < thresh else "." for _ in range(m)] for i in range(n)]
    a=time.time()

    solve(n,m,grid)
    print(time.time()-a)
    break