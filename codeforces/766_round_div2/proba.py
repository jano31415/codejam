def solve(grid, r,c):
    r=r-1
    c=c-1
    if not any("B" in row for row in grid):
        return -1
    if grid[r][c] == "B":
        return 0
    for i in range(m):
        if grid[r][i] == "B":
            return 1
    for i in range(n):
        if grid[i][c] == "B":
            return 1
    return 2



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,m,r,c  = [int(x) for x in input().decode().strip().split()]
        grid=[]
        for i in range(n):
            row = input().decode().strip()
            assert len(row) == m
            grid.append(row)
        assert len(grid) == n

        res=solve(grid, r,c)
        print(res, flush=True)
