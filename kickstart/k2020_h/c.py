def solve(players):
    x_players = sorted(players, key=lambda x: x[1])
    med = x_players[len(x_players)//2][1]
    res = 0
    for x in x_players:
        res += abs(med-x[1])
    return res + find_best_x([x[0] for x in x_players])

def find_best_x(x_list):
    sorted_l = sorted(x_list)
    # med = sorted_l[len(sorted_l)//2]
    start = -10**9 #sorted_l[0]
    end = 10**9 #sorted_l[-1]

    while start != end:
        # print(start,end)
        mid = (end + start) // 2
        if start + 1 == end:
            return min(query(sorted_l, start), query(sorted_l, end))
        left = query(sorted_l, mid)
        right = query(sorted_l, mid+1)
        if left <= right:
            end = mid
        else:
            start = mid
    minres = query2(sorted_l, start)
    # min_i = 0
    # for i in range(start,end):
    #     tmp = query(sorted_l, i)
    #     if tmp < minres:
    #         minres = tmp
    #         min_i = i
    return minres


def query2(sorted_l,mid):
    return sum([abs(player - endpoint) for player, endpoint in zip(range(mid, mid+len(sorted_l)), sorted_l)])

def query(sorted_l, mid):
    suml = 0
    for player, endpoint in zip(range(mid, mid+len(sorted_l)), sorted_l):
        suml += abs(player - endpoint)
    return suml


def main():
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        l = []
        for i in range(n):
            x, y = [int(x) for x in input().split(" ")]
            l.append((x,y))
        res = solve(l)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()
# print(query([1,4,5], 3))
