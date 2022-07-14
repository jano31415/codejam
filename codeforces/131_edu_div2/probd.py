import math
def solve(n,perm):
    zeroes = []
    res=[0]*n
    ratio =[]
    for i,x in enumerate(perm):
        if x == 0:
            zeroes.append(i+1)
        else:
            ratio.append(((i+1)/x, -(i+1)))
    ratio.sort(reverse = False)
    alln = set(list(range(1,n+1)))
    k=1
    j=0
    gaps=set()
    try_gaps=True
    while j < len(ratio):
        id = -ratio[j][1]
        if try_gaps:
            try_gaps = False
            for k1 in gaps:
                if id // k1 == perm[id - 1]:
                    res[id - 1] = k1
                    j += 1
                    gaps.remove(k1)
                    alln.remove(k1)
                    try_gaps=True
                    break
        else:
            if id//k == perm[id-1]:
                res[id-1] = k
                j+=1
                alln.remove(k)
                k+=1
                try_gaps=True
            else:
                gaps.add(k)
                k+=1
            if k > n+1:
                return 1

    remaining = sorted(list(alln))

    for k in range(n-len(ratio)):
        res[zeroes[k]-1] = remaining[k]
    return " ".join([str(x) for x in res])
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        perm = [int(x) for x in input().decode().strip().split()]

        res=solve(n,perm)
        print(res)

