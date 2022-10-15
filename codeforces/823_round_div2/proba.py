def solve(n,c,orbits):
    orb_dict = {}
    for x in orbits:
        if x not in orb_dict:
            orb_dict[x] = 0
        orb_dict[x] += 1
    tot=0
    for orb in orb_dict:
        orb_val = orb_dict[orb]
        if orb_val >= c:
            tot+=c
        else:
            tot+=orb_val
    return tot

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,c = [int(x) for x in input().decode().strip().split()]
        orbits = [int(x) for x in input().decode().strip().split()]

        res=solve(n,c, orbits)
        print(res)

