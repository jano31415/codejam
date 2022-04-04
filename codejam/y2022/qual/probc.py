
def solve(N, dice):
    dice.sort()
    cur = 0
    for i in range(N):
        if dice[i] > cur:
            cur += 1
    return cur

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        dice = [int(x) for x in input().split(" ")]
        res=solve(N, dice)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)
