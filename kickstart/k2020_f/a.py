import math
def solve(A, X, queue):
    withdraw = [(i, math.ceil(queue[i-1]/X)) for i in range(1, len(queue)+1)]
    res_tup = sorted(withdraw, key=lambda tup: (tup[1], tup[0]))
    # print(res_tup)
    res = [x[0] for x in res_tup]
    return res


def main():
    T = int(input())
    for t in range(1, T+1):
        A, X = [int(x) for x in input().split(" ")]
        queue = [int(x) for x in input().split(" ")]
        res = solve(A, X, queue)
        # print(res)
        res = [str(x) for x in res]
        res_str = " ".join(res)
        print("Case #{t}: {res}".format(t=t, res=res_str), flush=True)

main()