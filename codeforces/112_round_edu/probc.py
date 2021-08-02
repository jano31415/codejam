def solve(n, board):
    bob_score=[0]*n
    bot=0
    top = sum(board[0])
    for i in range(n):
        top -= board[0][i]
        bob_score[i] = max(bot, top)
        bot += board[1][i]
    return min(bob_score)




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        row1=[int(x) for x in input().decode().strip().split(" ")]
        row2=[int(x) for x in input().decode().strip().split(" ")]
        res1 = solve(n, [row1,row2])
        print(res1)
