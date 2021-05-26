def solve(n,k,s):
    restart = 1 + n + (k-1)
    goback = (k-s) + (n-s+1) + (k-1)

    return min(restart, goback)

def main():
    T = int(input())
    for t in range(1, T+1):
        n,k,s = [int(x) for x in input().split(" ")]
        res = solve(n,k,s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()