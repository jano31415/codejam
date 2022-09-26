
def solve(n, fabrics):
    f_ada = [(f[0],f[2]) for f in fabrics]
    f_charles = [(f[1],f[2]) for f in fabrics]
    f_ada.sort()
    f_charles.sort()
    tot = 0
    for i in range(n):
        if f_ada[i][1] == f_charles[i][1]:
            tot+=1
    return tot


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        fabrics = [0]*n
        for i in range(n):
            c,d,u = input().split()
            d,u = int(d), int(u)
            fabrics[i] = (c,d,u)

        res = solve(n, fabrics)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
