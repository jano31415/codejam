import numpy as np

def solve(cs,ms,ys,ks):
    cmin = min(cs)
    mmin = min(ms)
    ymin = min(ys)
    kmin = min(ks)
    tot = cmin +mmin + ymin + kmin
    if tot < 10**6:
        return "IMPOSSIBLE"
    ink = 10**6
    res = [0]*4
    avail = [cmin, mmin, ymin, kmin]
    for i in range(4):
        cur = avail[i]
        if ink <= cur:
            res[i] = ink
            ink = 0
            break
        else:
            res[i] = cur
            ink -= cur
    assert sum(res) == 10**6
    return " ".join([str(x) for x in res])

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        cs = []
        ms = []
        ys = []
        ks = []
        for d in range(3):
            c, m, y, k = [int(x) for x in input().split(" ")]
            cs.append(c)
            ms.append(m)
            ys.append(y)
            ks.append(k)
        res=solve(cs,ms,ys,ks)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)
