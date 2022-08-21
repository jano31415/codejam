# trying just test set 1 because its probably difficult.
# after reading it sounds like dp over all crossing and time.

from copy import deepcopy
def solve(N, P,M,Ar,Ac, directions):
    if P != 0:
        msg = "Let God have mercy on my soul"
    dp = [["inf"]*N for i in range(N)]
    dp[Ar-1][Ac-1] = 0

    for t in range(M):
        dpnext = deepcopy(dp) # do nothing for one timestep
        for r in range(N):
            for c in range(N):
                if dp[r][c] == "inf":
                    continue
                for sign, dc, updownleftright in directions:
                    updown, leftright = updownleftright
                    new_row = r+updown
                    new_col = c+leftright
                    rowgood= (new_row < N) and (new_row >= 0)
                    colgood = (new_col < N) and (new_col >= 0)
                    new_coins = calc(dp[r][c], sign, dc)
                    if rowgood and colgood:
                        if dpnext[new_row][new_col] != "inf":
                            if dpnext[new_row][new_col] < new_coins:
                                dpnext[new_row][new_col] = new_coins
                        else:
                            dpnext[new_row][new_col] = new_coins
        dp = dpnext
    l =[]
    for row in dp:
        for v in row:
            if v != "inf":
                l.append(v)
    return max(l)
def calc(coins, sign, dc):
    if sign == "+":
        return coins +dc
    elif sign == "-":
        return coins - dc
    elif sign == "*":
        return coins * dc
    else:
        return coins // dc

# 20 * 10 * 10 * 4 = 8k


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        N, P, M, Ar, Ac = [int(x) for x in input().split()]
        Ar, Ac = int(Ar), int(Ac)
        directions = []
        #North, East, West, South
        updown = [(-1,0), (0,1), (0,-1), (1,0)]
        for i in range(4):
            sign, c = input().split()
            directions.append((sign, int(c), updown[i]))
        res = solve(N, P,M,Ar,Ac, directions)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

