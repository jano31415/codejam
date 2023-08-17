import math
import random


def solve(n, perm):
    dyn_perm = [0]*n
    # first element always losing
    # 1 alice winning, bob losing
    # 0 bob winning, alice losing
    dyn_perm[0]=0
    smallest_perm = perm[0]
    smallest_losing_perm = None
    for j in range(1,n):
        if smallest_perm > perm[j]:
            dyn_perm[j]=0
        elif smallest_losing_perm is None or smallest_losing_perm > perm[j]:
            dyn_perm[j]=1
        smallest_perm = min(smallest_perm, perm[j])
        if dyn_perm[j]==1:
            if smallest_losing_perm is None:
                smallest_losing_perm = perm[j]
            else:
                smallest_losing_perm = min(smallest_losing_perm, perm[j])

    return sum(dyn_perm)

def solve_slow(n, perm):
    dyn_perm = [0] * n
    # first element always losing
    # 1 alice winning, bob losing
    # 0 bob winning, alice losing
    dyn_perm[0] = 0
    for j in range(1, n):
        for new_move_i in range(j):
            moves = [new_move_i for new_move_i in range(j) if perm[new_move_i] < perm[j]]
            if len(moves) == 0:
                dyn_perm[j] = 0
            elif all([dyn_perm[new_move_i] == 0 for new_move_i in moves]):
                dyn_perm[j] = 1
    return sum(dyn_perm)
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        perm = [int(x) for x in input().decode().strip().split()]
        res=solve(n, perm)
        # print(solve_slow(n,perm))
        print(res)

# import numpy
# for _ in range(100):
#     n=random.randint(1,10)
#     perm = numpy.random.permutation(n)
#     a=solve_slow(n,perm)
#     b=solve(n,perm)
#     if a!=b:
#         print(perm)