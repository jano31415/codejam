def solve(n,l, ants):
    ants.sort()
    times = [x if d ==0 else l-x for x,d,ai in ants]
    order= [ai for x,d,ai in ants]
    prefix_sum = [0]*n
    cur = 0
    for i, ant in enumerate(ants):
        p,d,ai = ant
        cur += (1-d)
        prefix_sum[i] = cur
    prefix_sum_left = [0] * n
    cur = 0
    for i, ant in enumerate(ants[::-1]):
        p, d,ai = ant
        cur += d
        prefix_sum_left[i] = cur
    sol = [0]*n
    for i, ant in enumerate(ants):
        p,d,ai = ant
        if d == 1:
            sol[i + prefix_sum[-1] - prefix_sum[i]] = times[i]
    for i, ant in enumerate(ants[::-1]):
        ni = n-1-i
        p,d,ai = ant
        if d == 0:
            sol[ni - prefix_sum_left[-1] + prefix_sum_left[i]] = times[ni]

    for i,x in enumerate(sol):
        if x == 0:
            sol[i] = times[i]
    sol_order = list(zip(sol,order))
    sol_order.sort()

    return " ".join([str(ant_name+1) for time,ant_name in sol_order])


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n, l = [int(x) for x in input().split()]
        ants =[]
        for i in range(n):
            p, d = [int(x) for x in input().split()]
            ants.append((p,d,i))

        res = solve(n,l, ants)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)