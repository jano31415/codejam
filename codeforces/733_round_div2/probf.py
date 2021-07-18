inv10 = 3973
mod = 31607
# r1 = 1/4
# c1 = 1/4 * 1/2
# c2 = 1/4 * 1/2
# r2 = 1/4 * 1/2 * 1/2
# d1 = 1/4 * 1/2*1/2
# d2 = d1

# r1 = 1/4
# r2 = 1/4 * 3/4
# c1 = 1/4 * 1/2 * 1/2
# c2 = 1/4 * 1/2 * 1/2
# d1 = 1/4 * 1/2*1/2
# d2 = d1
def inv(a,mod):
    return pow(a,mod-2,mod)

def solve(grid):
    n = len(grid)
    row_prob1=[0]*n
    row_prob2 = [0]*n
    not_before = 1
    for i,row in enumerate(grid):
        p = 1
        for r in row:
            p= (p*r *inv10) % mod
        row_prob2[i] = (p * not_before) %mod
        row_prob1[i] = p

        not_before = (not_before * ((1 - p)%mod)) % mod # * (1-p)

    col_prob1 = [0]*len(grid)
    col_prob2 = [0]*len(grid)
    not_before = 1
    for j in range(len(grid)):
        col = [row[j] for row in grid]
        p=1
        for c in col:
            p= (p*c *inv10) % mod
        col_prob1[j]=p

        for i,row in enumerate(grid):
            row_prob = (row_prob1[i] * inv(grid[i][j], mod) * 10**4)%mod
            p= (p * (1- row_prob)%mod)
        col_prob2[j] = (p * not_before) % mod
        not_before = (not_before * ((1 - col_prob1[j])%mod)) % mod # * (1-p)

    p=1
    for i in range(len(grid)):
       p *= grid[i][i]
    diagp1 = p
    for i in range(len(grid)):
       p *= (1 - row_prob1[i]//grid[i][i])
       p *= (1 - col_prob1[i]//grid[i][i])
    diagp2 = p

    for i in range(len(grid)):
       p *= grid[i][n-i-1]
       p *= (1 - row_prob1[i]//grid[i][n-i-1])
       p *= (1 - col_prob1[i]//grid[i][n-i-1])
    if n%2 == 1:
        anti_diag = p * (1-diagp1//grid[n//2][n//2])
    else:
        anti_diag = p

    return sum(row_prob2) + sum(col_prob2) + diagp2 + anti_diag


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    grid = []
    for t in range(T):
        row =[int(x) for x in input().decode().strip().split(" ")]
        grid.append(row)
    res1 = solve(grid)
    print(res1)
