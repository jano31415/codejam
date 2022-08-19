def solve(n, m, grid):
    max_moves = sum([sum(row) for row in grid])
    if max_moves == n*m:
        return max_moves-2

    if max_moves == 0:
        return 0
    for row in grid:
        for i in range(len(row)):
            if i != len(row)-1:
                if row[i] == 0 and row[i+1] == 0:
                    return max_moves
    for i in range(len(grid)):
        if i != len(grid) - 1:
            for j in range(m):
                if grid[i][j] == 0 and grid[i+1][j] == 0:
                    return max_moves

    for i in range(len(grid)):
        if i != len(grid) - 1:
            for j in range(m):
                if j != m-1:
                    if grid[i][j+1] == 0 and grid[i + 1][j] == 0:
                        return max_moves
                    if grid[i][j] == 0 and grid[i + 1][j+1] == 0:
                        return max_moves
    return max_moves-1



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        grid=[]
        for i in range(n):
            row = [int(x) for x in input().decode().strip()]
            grid.append(row)
            assert len(row) == m
        assert len(grid) == n

        res=solve(n, m, grid)
        print(res)

# for i in range(1024, 1200):
#     for j in range()