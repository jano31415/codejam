import math
import random


def solve(n,a,b):
    if n == 1:
        return 0, []
    ab = list(zip(a,b))
    abi = [(aibi[0],aibi[1],i) for i,aibi in enumerate(ab)]
    abi.sort()
    cura, curb, j = abi[0]
    for i in range(len(ab)):
        newa ,newb, _ = abi[i]
        if newa < cura or newb < curb:
            return -1, None
        cura = newa
        curb = newb
    moves = []
    end_start = [(end_index, abi[end_index][2]) for end_index in range(n)]
    beginning = list(range(n))
    for i in range(n):
        start_i = end_start[i][1]
        cur_i = beginning.index(start_i)
        if i != cur_i:
            moves.append((str(i+1), str(cur_i+1)))
            tmp = beginning[i]
            beginning[i] = beginning[cur_i]
            beginning[cur_i]=tmp
    assert beginning == [x[1] for x in end_start]
    return len(moves), moves
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a = [int(x) for x in input().decode().strip().split()]
        b = [int(x) for x in input().decode().strip().split()]
        res1, moves= solve(n,a,b)
        print(res1)
        if res1 > 0:
            for m1,m2 in moves:
                print(f"{m1} {m2}")
#
# import random
# for x in range(100):
#     n = 10
#     a=[random.randint(0,10) for x in range(n)]
#     b=[random.randint(0,10) for x in range(n)]
#     solve(n,a,b)
