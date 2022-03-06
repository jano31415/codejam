def solve(n,k,candies):
    tot = sum(candies)
    return tot % k


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n, k = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        res = solve(n,k,candies)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)