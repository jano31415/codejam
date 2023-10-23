def solve(R, C, board):
    # bfs type
    whites = []
    seen={}
    for ri,row in enumerate(board):
        for ci,c in enumerate(row):
            if c == "W":
                loc = (ri,ci)
                seen[loc] = 0
                whites.append(loc)
    # bfs
    while len(whites) > 0:
        group_empty = set()
        w = whites.pop()
        if seen[w] == 1:
            continue
        group = [w]
        while len(group) > 0:
            w = group.pop()
            seen[w] = 1
            neighbours = get_neighbours(w, R, C)
            for nr,nc in neighbours:
                b = board[nr][nc]
                if  b == "W":
                    if seen[(nr,nc)] == 0:
                        group.append((nr,nc))
                elif b == ".":
                    group_empty.add((nr,nc))
                    # print(f"{(nr,nc)} empty for group {w}")

        if len(group_empty) == 1:
            return "YES"
        if len(group_empty) == 0:
            print("Found a group that shouldnt exist, buggy")
    return "NO"

def get_neighbours(w, R, C):
    wr, wc = w
    neighbours = [(wr-1,wc), (wr+1, wc), (wr, wc-1), (wr, wc+1)]
    neighbours = [(r,c) for r,c in neighbours if r>=0 and r<R and c>=0 and c<C]
    return neighbours

def get_neighbours_t():
    pass


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_a.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        R,C = [int(x) for x in input().decode().strip().split(" ")]
        board = []
        for r in range(R):
            row = [x for x in input().decode().strip()]
            board.append(row)
            assert len(row) == C
        assert len(board) == R
        res1=solve(R, C, board)
        print(res1)
        with open("out_a.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")

# from random import randint
# R=19
# C=19
# board=[[randint(0,3) for i in range(R)] for _ in range(C)]
# mapx={0:"B", 1:"B",2:"B", 3:"B"}
# board = [[mapx[x] for x in row] for row in board]
# import time
# a=time.time()
# solve(R,C, board)
# print(time.time() -a)