def solve(n,k):
    board=[["."]*n for _ in range(n)]
    start = 0
    for i in range(k):
        if start >= n:
            print(-1, flush=True)
            return
        board[start][start] = "R"
        start+=2
    for i in range(n):
        print("".join(board[i]), flush=True)

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]

        res=solve(n,k)
