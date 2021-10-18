def solve(N,D,C,M,s):
    for i,si in enumerate(s):

        if si == "C":
            if C == 0:
                for j in range(i,len(s)):
                    if s[j] == "D":
                        return "NO"
                return "YES"
            C-=1
        elif si == "D":
            if D==0:
                return "NO"
            D-=1
            C+=M

    return "YES"


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        N, D, C, M = [int(x) for x in input().split(" ")]
        s = input("")


        res = solve(N,D,C,M,s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)