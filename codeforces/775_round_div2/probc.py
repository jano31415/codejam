from collections import defaultdict


def solve(n,m, grid):
    color_to_loc = defaultdict(list)
    for nrow, row in enumerate(grid):
        for ncol, x in enumerate(row):
                color_to_loc[x].append((nrow, ncol))

    # solve x
    tot=0
    for c in color_to_loc:
        onedim = [point[0] for point in color_to_loc[c]]
        tot+= count_one_dim(onedim)
    for c in color_to_loc:
        onedim = [point[1] for point in color_to_loc[c]]
        tot+= count_one_dim(onedim)
    return tot

def count_one_dim(onedim):
    onedim.sort()
    sumall = sum(onedim)
    nrpoints = len(onedim)
    this_tot = 0
    for i,x in enumerate(onedim):
        this_tot += max(0, sumall - nrpoints*x)
        nrpoints -= 1
        sumall -= x
    return this_tot
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline



    n,m = [int(x) for x in input().decode().strip().split()]
    grid = []
    for i in range(n):
        row = [int(x) for x in input().decode().strip().split()]
        grid.append(row)

    res=solve(n,m, grid)
    print(res)
