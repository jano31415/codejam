import math
def solve(N,A,B, units):
    tot = sum(units)
    min_trans = math.ceil(math.log2(tot))
    first_poss = max(min_trans * A, len(units)-1)
    for start_pos in range(first_poss, first_poss+1000):
        # print(start_pos)
        res = simulate(start_pos, A, B, units)
        if res:
            return start_pos+1  # zero based
    return "IMPOSSIBLE"

def simulate(start_pos, A, B, units):
    res = [0]*(start_pos+1)
    res[start_pos] = 1
    for j in reversed(range(start_pos+1)):
        if j <= len(units)-1:
            transmute_nr = res[j] - units[j]
            if transmute_nr < 0:
                return False
            if transmute_nr == 0:
                continue
            res[j] = units[j]
        else:
            transmute_nr = res[j]
            res[j] = 0

        if transmute_nr > 0:
            if j-A >= 0:
                res[j-A] += transmute_nr
            if j - B >= 0:
                res[j-B] += transmute_nr
    return True


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N,A,B = [int(x) for x in input().split(" ")]
        units = [int(x) for x in input().split(" ")]
        # import time
        # time1 = time.time()
        res = solve(N,A,B,units)
        # time2 = time.time()
        # print(time2-time1)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)