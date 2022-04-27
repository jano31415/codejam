def solve(n,p,grid):
    mins = [min(x) for x in grid]
    maxs = [max(x) for x in grid]
    dyn_min_max = [0]*len(grid)
    dyn_max_min = [0]*len(grid)
    dyn_min_max[0] = maxs[0]
    dyn_max_min[0] = maxs[0] + abs(maxs[0]-mins[0])
    for i in range(1, n):
        # 0 min then max
        from_max = dyn_min_max[i-1] + abs(maxs[i-1] - mins[i]) + abs(mins[i] - maxs[i])
        from_min = dyn_max_min[i-1] + abs(mins[i-1] - mins[i]) + abs(mins[i] - maxs[i])
        dyn_min_max[i] = min(from_max, from_min)

        from_max = dyn_min_max[i-1] + abs(maxs[i-1] - maxs[i]) + abs(maxs[i] - mins[i])
        from_min = dyn_max_min[i-1] + abs(mins[i-1] - maxs[i]) + abs(maxs[i] - mins[i])
        dyn_max_min[i] = min(from_max, from_min)

    return min(dyn_min_max[-1], dyn_max_min[-1])

T = int(input())
for t in range(1, T+1):
    n,p = [int(x) for x in input().split(" ")]
    grid=[]
    for i in range(n):
        grid.append([int(x) for x in input().split(" ")])
    res=solve(n,p,grid)
    print("Case #{i}: {res}".format(i=t, res=res), flush=True)
