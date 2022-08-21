# test only the substrings of lengths that n is divisible by.
# 13:55 success
def solve(n, p):
    s = []
    for i in range(n):
        s.append(p[i])
        if n%len(s) != 0:
            continue
        palin=True
        for j,sj in enumerate(s):
            if j > len(s)//2+1:
                break
            if s[j] != s[-(j+1)]:
                palin = False
        if not palin:
            continue
        issol=True
        for j,pj in enumerate(p):
            if p[j] != s[j%len(s)]:
                issol=False
                break
        if issol:
            return s


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        p = input()
        res = solve(n, p)
        res = "".join(res)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

