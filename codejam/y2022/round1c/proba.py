import numpy as np

def solve(n, towers):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for a in alph:
        at = [t for t in towers if a in t]
        if len(at) == 0:
            continue
        for x in at:
            s = x.find(a)
            e = x[::-1].find(a)
            if len(set(x[s:len(x)-e])) > 1:
                return "IMPOSSIBLE"
        # elif not all([t[0] == a or t[-1] == a for t in at]):
        #     return "IMPOSSIBLE"
        if len(at) > 1:
            enda = [x for x in at if x[-1] == a and x[0] != a]
            if len(enda) ==0:
                enda=[""]
            if len(enda) > 1:
                return "IMPOSSIBLE"
            endastr = enda[0]

            mida = [x for x in at if x[-1] == a and x[0] == a]
            mida = "".join(mida)
            if len(set(mida)) > 1:
                return "IMPOSSIBLE"
            mida = endastr + mida

            starta = [x for x in at if x[-1] != a and x[0] == a]
            if len(starta) ==0:
                starta=[""]
            if len(starta) > 1:
                return "IMPOSSIBLE"
            startstr = starta[0]

            new_tower = mida + startstr
            if len([x for x in at if x[-1] != a and x[0] != a]) > 0:
                return "IMPOSSIBLE"
            towers = [t for t in towers if a not in t]
            towers.append(new_tower)
    return "".join(towers)



if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        towers = [x for x in input().split(" ")]
        res = solve(n, towers)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)

