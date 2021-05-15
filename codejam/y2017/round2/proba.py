def solve(choc, N, P):
    if P == 2:
        res = solve2(choc, N)
    elif P == 3:
        res = solve3(choc, N)
    else:
        res = solve4(choc, N)
    return res

def solve2(choc, N):
    mod_sum = sum([x % 2 for x in choc])
    case2 = mod_sum//2
    return N - case2


def solve3(choc, N):
    choc_mod = [x % 3 for x in choc]
    counts = [choc_mod.count(x) for x in range(3)]
    diff = abs(counts[1]-counts[2])
    case3 = diff//3
    if diff%3 > 0:
        case3+=1
    return counts[0] + min(counts[1], counts[2]) + case3


def solve4(choc, N):
    choc_mod = [x % 4 for x in choc]
    counts = [choc_mod.count(x) for x in range(4)]
    case2 = counts[2]//2
    diff = abs(counts[1] - counts[3])
    case3 = diff // 4
    if (diff % 4 == 3) and (counts[2] % 2 == 1):
        case3 += 2
    elif diff % 4 >= 1:
        case3 += 1
    elif counts[2] % 2 == 1:
        case2 += 1

    return counts[0] + min(counts[1], counts[3]) + case3 + case2


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N,P = [int(x) for x in input().split(" ")]
        choc = [int(x) for x in input().split(" ")]
        res = solve(choc, N, P)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

