from itertools import permutations
def solve(e,w,lifts):
    perms =[]
    for lift in lifts:
        base = []
        for i, l in enumerate(lift):
            base.append(str(i) * l)
        base = "".join(base)
        tmp_perm = set()
        for p in permutations(base):
            tmp_perm.add("".join(p))
        perms.append(tmp_perm)

    dyn= [{p:10**9 if i !=0 else len(p) for p in perms[i]} for i in range(e)]

    for step in range(e-1):
        for p1 in dyn[step]:
            for p2 in dyn[step+1]:
                p_diff = get_pdiff(p1, p2)
                dyn[step+1][p2] = min(dyn[step+1][p2], dyn[step][p1] + p_diff)
    return min([dyn[-1][x] for x in dyn[-1]]) + sum(lifts[-1])

cache={}
def get_pdiff(p1, p2):
    if (p1,p2) in cache:
        return cache[(p1, p2)]
    for i in range(len(p1)):
        if i > len(p2)-1 or p1[i] != p2[i]:
            res = len(p1) + len(p2) - 2*i
            cache[(p1, p2)] = res
            return res
    res = len(p2)-len(p1)
    cache[(p1, p2)] = res
    return res

def get_pdiff2(p1, p2):

    for i in range(len(p1)):
        if i > len(p2)-1 or p1[i] != p2[i]:
            return len(p1) + len(p2) - 2*i
    return len(p2)-len(p1)

if __name__ == "__main__":
    T = int(input())
    import time
    a= time.time()
    for t in range(1, T+1):
        e, w = [int(x) for x in input().split(" ")]
        lifts = []
        for i in range(e):
            lift = [int(x) for x in input().split(" ")]
            lifts.append(tuple(lift))
        res = solve(e,w, lifts)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)
    print(time.time()-a)
