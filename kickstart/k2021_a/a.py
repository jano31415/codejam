
def solve(N, K, s):

    tot = len(s)//2
    count = 0
    for i in range(tot):

        if s[i] != s[len(s)-i-1]:
            count += 1
    return abs(K - count)

def main():
    T = int(input())
    for t in range(1, T + 1):
        N, K = [int(x) for x in input().split(" ")]
        s = input()
        res = solve(N, K, s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)


main()