import math
def solve(n):
    d =2
    minx = 1
    used = set()
    perm = []
    while len(used) != n:
        if minx not in used:
            perm.append(str(minx))
            used.add(minx)
            tmp = 2*minx
            while tmp <= n:
                used.add(tmp)
                perm.append(str(tmp))
                tmp = 2*tmp
        minx+=1
    assert len(perm) == n
    print(d)
    return " ".join(perm)
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        res=solve(n)
        print(res)

