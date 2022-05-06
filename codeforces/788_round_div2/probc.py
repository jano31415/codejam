import math
def solve(n, a, b, d):
    ab_cycles = [0]*n
    inv_b = [0]*(n+1)
    cycle_to_index = {}

    nr_cycles = 1
    for i,x in enumerate(b):
        inv_b[x]=i

    for i,x in enumerate(a):
        if ab_cycles[i] != 0:
            continue
        ab_cycles[i] = nr_cycles
        if nr_cycles not in cycle_to_index:
            cycle_to_index[nr_cycles] = []
        cycle_to_index[nr_cycles].append(i)
        nexti = inv_b[x]
        ab_cycles[nexti] = nr_cycles
        if nexti != i:
            cycle_to_index[nr_cycles].append(nexti)
        while nexti != i:
            nexti = inv_b[a[nexti]]
            ab_cycles[nexti] = nr_cycles
            if nexti != i:
                cycle_to_index[nr_cycles].append(nexti)
        nr_cycles+=1
    max_cycle = max(ab_cycles)
    cycles = set(range(1, max_cycle+1))
    for i in range(1, max_cycle+1):
        count=0
        for j in cycle_to_index[i]:
            if a[j] == b[j]:
                count+=1
            if d[j] != 0:
                count = len(cycle_to_index[i])
                break
        if count == len(cycle_to_index[i]):
            cycles.remove(i)

    different_cycles = len(cycles)
    mod = 10**9+7
    return pow(2, different_cycles, mod)


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a = [int(x) for x in input().decode().strip().split()]
        b = [int(x) for x in input().decode().strip().split()]
        d = [int(x) for x in input().decode().strip().split()]
        assert len(a) == n
        assert len(b) == n
        assert len(d) == n

        res=solve(n, a, b, d)
        print(res)

