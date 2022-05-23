import math
import random


def solve(n,doors_top, doors_right, queries):
    topdoor = [0]*n
    rightdoor = [0]*n
    for i in range(1,n):
        corner = i+1
        i_1_up = doors_right[i-1][0]
        i_1_right = doors_right[i-1][1]
        i_up = doors_right[i][0]
        i_right = doors_right[i][1]
        top_top = 1 + abs(i_right - i_1_right)
        right_top = 1 + abs(corner - i_1_up) + abs(corner - i_right)
        top_right = 1 + abs(corner - i_1_right) + abs(corner - i_up)
        right_right = 1 + abs(i_1_up - i_up)

        topdoor[i] = min((topdoor[i-1] + top_top), (rightdoor[i-1], right_top))
        rightdoor[i] = min(rightdoor[i-1] +right_right, topdoor[i-1] +top_right)

    for q in queries:
        ax, ay, bx, by = q
        kstart = max(ax, ay)
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n = int(input().decode().strip())
    doors_top = []
    doors_right =[]
    for i in range(n-1):
        d1x,d1y,d2x,d2y = [int(x) for x in input().decode().strip().split()]
        doors_top.append((d1x,d1y))
        assert d1x == i+1
        doors_right.append((d2x,d2y))
        assert d2y == i+1
    q = int(input().decode().strip())
    queries=[]
    for i in range(q):
        ax,ay,bx,by = [int(x) for x in input().decode().strip().split()]
        queries.append((ax,ay,bx,by))
    res1= solve(n,doors_top, doors_right, queries)
