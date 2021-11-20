def solve(s, f):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph_to_index = {alph[i]:i for i in range(26)}
    tot = 0
    for si in s:
        min_change = 26
        for fi in f:
            direct = abs(alph_to_index[fi] - alph_to_index[si])
            this_change = min(direct, 26-direct)
            if this_change < min_change:
                min_change = this_change
        tot+= min_change
    return tot




if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        s = input()
        f = input()


        res = solve(s,f)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)