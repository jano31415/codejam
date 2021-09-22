def solve(n,s):
    bins_indices= []
    for i,si in enumerate(s):
        if si == "1":
            bins_indices.append(i+1)
    cur_i = 0
    curr = bins_indices[cur_i]
    tot = 0
    for i in range(1,n+1):
        if cur_i < len(bins_indices) -1:
            dist_bef = abs(i-bins_indices[cur_i])
            dist_aft = abs(i-bins_indices[cur_i+1])
            dist = dist_bef
            if dist_aft <= dist_bef:
                cur_i += 1
                dist = dist_aft
            tot += dist
        else:
            tot += abs(i-bins_indices[cur_i])
    return tot


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        s = input("")


        res = solve(n,s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)