# 23min reading, writing and uploading

def solve(N, K, P, all_stacks):
    # dynamic programming
    # save best way to take p plates from first k stacks
    #int,int -> int
    all_stacks = to_cumsum(all_stacks)
    dyn_cache = [[0]*(P+1) for _ in range(N)]
    for n in range(N):
        for k in range(min(K+1, P+1)):
            if n == 0:
                dyn_cache[n][k] = all_stacks[0][k]
            else:
                for p in range(P+1):
                    if p+k > P:
                        break
                    tmp = all_stacks[n][k] + dyn_cache[n-1][p]
                    if tmp > dyn_cache[n][k+p]:
                        dyn_cache[n][k+p] = tmp

    return dyn_cache[N-1][P]

import numpy as np
def to_cumsum(all_stacks):
        return [[0] + list(np.cumsum(stack)) for stack in all_stacks]

def main():
    T = int(input())
    for t in range(1, T+1):
        N,K, P = [int(x) for x in input().split(" ")]
        all_stacks = []
        for i in range(N):
            stack = [int(x) for x in input().split(" ")]
            all_stacks.append(stack)
        res = solve(N, K, P, all_stacks)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()