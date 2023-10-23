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
    group_size = {"no_play":0}
    for w in whites:
        group_empty = set()
        if seen[w] == 1:
            continue
        all_group = {w}
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
                        all_group.add((nr,nc))
                elif b == ".":
                    group_empty.add((nr,nc))
                    # print(f"{(nr,nc)} empty for group {w}")

        if len(group_empty) == 1:
            play_this = list(group_empty)[0]
            if play_this not in group_size:
                group_size[play_this] = 0
            group_size[play_this] += len(all_group)
        # if len(group_empty) == 0:
        #     print("Found a group that shouldnt exist, buggy")
    return max(group_size.values())

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
    with open("out_a2.txt", "w") as f:
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
        with open("out_a2.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")

# from random import randint
# R=3000
# C=3000
# board=[[randint(0,3) for i in range(R)] for _ in range(C)]
# mapx={0:".", 1:"W",2:"W", 3:"B"}
# board = [[mapx[x] for x in row] for row in board]
# import time
# a=time.time()
# solve(R,C, board)
# print(time.time() -a)