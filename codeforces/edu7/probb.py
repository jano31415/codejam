def solve(n,s):
    one_players = s.count("1")
    two_players = s.count("2")
    if two_players in [1,2]:
        return "NO", []
    player2=[]
    for i,p in enumerate(s):
        if p == "2":
            player2.append(i)
    grid = [["=" for _ in range(len(s))] for _2 in range(len(s))]
    for i in range(n):
        grid[i][i] = "X"

    for i,p in enumerate(player2):
        j = i+1
        if j == len(player2):
            j = 0
        grid[p][player2[j]] = "+"
        grid[player2[j]][p] = "-"

    return "YES",grid

import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s=input().decode().strip()
        res, grid = solve(n,s)
        print(res)
        if len(grid) > 0:
            for g in grid:
                print("".join(g))

