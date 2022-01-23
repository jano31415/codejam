#DRAFT
import math
def solve(n,grid):
    if n==2:
        return grid[0][0]^grid[0][1]
    tot = 0
    grid2 =[[0]*n for _ in range(n)]
    for j,row in enumerate(grid):
        for i,x in enumerate(row):
            if (i)%2== j%2:
                tot^=x
                mark_grid(grid2, i, j, n)
    # for j,row in enumerate(grid):
    #     for i,x in enumerate(row):
    #             tot^=x
    #             mark_grid(grid2, i, j, n)

    print(grid2)
    return tot

def mark_grid(grid2,i,j,n):
    if i-1 >= 0:
        grid2[i-1][j] +=1
    if i+1 < n:
        grid2[i+1][j] +=1
    if j-1 >=0:
        grid2[i][j-1] +=1
    if j+1 < n:
        grid2[i][j+1] +=1





import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        grid =[]
        for _ in range(n):
            grid.append([int(x) for x in input().decode().strip().split()])

        res1=solve(n,grid)
        print(res1, flush=True)
