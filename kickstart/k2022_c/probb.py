def solve(n,x,y):
    imp ="IMPOSSIBLE"
    tot = ((n+1) * n)//2
    if (tot*y) % (x+y) != 0:
        return imp, None, None
    b = (tot*y) // (x+y)
    a = tot - b
    if a < 0:
        return "IMPOSSIBLE"
    res = 0
    cur=n
    sol=[]
    while (res + cur) < a:
        res+=cur
        sol.append(str(cur))
        cur-=1
        if cur < 0:
            return "IMPOSSIBLE"
    if a - res <= cur:
        if res != a:
            sol.append(str(a-res))
    return "POSSIBLE", len(sol), sol

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n,x,y= [int(x) for x in input().split()]
        res, a, sol = solve(n,x,y)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        if a is not None:
            print(a, flush=True)
            print(" ".join(sol), flush=True)