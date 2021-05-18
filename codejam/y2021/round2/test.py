# just some warmup
def solve(D, prog):
    dmg_done = get_dmg_prog(prog)
    if dmg_done<=D:
        return 0
    count = 0
    while True:
        new_prog = find_swap(prog)
        count += 1
        if get_dmg_prog(new_prog) <= D:
            return count
        if new_prog == prog:
            return "IMPOSSIBLE"
        prog = new_prog


def get_dmg_prog(prog):
    d=1
    tot_d = 0
    for i,x in enumerate(prog):
        if x == "S":
            tot_d+=d
        else:
            d = 2*d
    return tot_d


def find_swap(prog):
    new_prog = prog
    for i in reversed(range(1,len(prog))):
        if prog[i-1] == "C" and prog[i] == "S":
            return prog[:i-1] + "SC" + prog[i+1:]
    return new_prog


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        D,prog = input().split(" ")
        D = int(D)
        res = solve(D, prog)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)