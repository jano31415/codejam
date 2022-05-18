def solve(n, k):
    imp = "IMPOSSIBLE"
    if k < n-1:
        return imp
    if k % 2 == 1:
        return imp


    # path = []
    mid = n//2 + 1
    xmax = n
    tot=0
    full_circle_cache = [0]*(n+1)
    full_circle_cache[mid] = n**2
    depth=0
    while tot < n**2-1:
        circle = 4 * (xmax - 1)
        full_circle_cache[depth]=tot
        tot+=circle
        depth+=1
        xmax -=2
    full_circle_cache[depth]=tot
    # sol=[]
    # sol_pos=(1,1)
    sol_pos, grid = get_sol_pos2(n, k)
    print(sol_pos)
    _, grid = get_sol_pos1(n, k)
    print(_)
    print(grid)
    solx = sol_pos[0]
    soly = sol_pos[1]
    sol=[]
    grid = [[0]*7 for _ in range(7)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = get_grid(full_circle_cache, i,j)
    while abs(mid-solx) + abs(mid-soly) != 0:
        for dirx,diry in [(1,0), (0,1), (-1,0), (0,-1)]:
            new_curx =  solx + dirx
            new_cury = soly + diry
            if abs(mid-solx) + abs(mid-soly) > abs(mid-new_curx) + abs(mid-new_cury):
                if get_grid(full_circle_cache, solx-1, soly-1) < get_grid(full_circle_cache,new_curx-1, new_cury-1):
                    old_pos = get_grid(full_circle_cache, solx-1, soly-1)
                    new_pos = get_grid(full_circle_cache, new_curx-1,new_cury-1)
                    if new_pos != old_pos+1:
                        sol.append((old_pos, new_pos))
                    solx = new_curx
                    soly = new_cury
    return sol

def get_sol_pos2(n,k):
    xmax=n
    ymax=n
    dist=0
    mid = n//2 + 1
    curx=1
    cury=1
    while True:
        circle = 4*(xmax-1)
        if dist + circle + abs(curx - mid) + abs(cury - mid) > k:
            break
        curx += 1
        cury += 1
        dist += circle
        xmax -= 2
        ymax -= 2
    for i in range(xmax-1):
        if dist + abs(curx - mid) + abs(cury - mid) == k:
            return (curx, cury), None
        curx+=1
        dist+=1
    for i in range(ymax-1):
        if dist + abs(curx - mid) + abs(cury - mid) == k:
            return (curx,cury), None
        cury+=1
        dist+=1
    for i in range(xmax-1):
        if dist + abs(curx - mid) + abs(cury - mid) == k:
            return (curx,cury), None
        curx-=1
        dist+=1
    for i in range(ymax-2):
        if dist + abs(curx - mid) + abs(cury - mid) == k:
            return (curx,cury), None
        cury-=1
        dist+=1
    return (curx, cury), None

def get_grid(full_circle_cache, xi, yj):
    mid = n//2 + 1
    inner_depth = max(abs(mid - xi), abs(mid - yj))
    outer_depth = mid - inner_depth
    full_circle = full_circle_cache[outer_depth]
    tot=full_circle
    if xi == mid - inner_depth:
        tot+= yj - outer_depth
        return tot
    else:
        tot+= 2*(inner_depth-1)

    if yj == mid + inner_depth:
        tot+= xi - outer_depth
        return tot
    else:
        tot+= 2*(inner_depth-1)

    if xi == mid + inner_depth:
        tot+= outer_depth+ 2*inner_depth - yj
        return tot
    else:
        tot+= 2*(inner_depth-1)

    if yj == mid + inner_depth:
        tot+= outer_depth+ 2*inner_depth - xi
        return tot
    else:
        tot+= 2*(inner_depth-1)

    return tot

def get_sol_pos1(n,k):
    curx, cury = 1, 1
    mid = n//2 + 1
    dist = 1
    xmax=n
    xmin=0
    ymin=0
    ymax=n
    grid = [[0]*n for i in range(n)]
    grid[0][0]=1
    grid[mid-1][mid-1] = n**2
    while dist < n ** 2 - 1:
        for dirx, diry in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            while (xmin < curx + dirx <= xmax) and (ymin < cury + diry <= ymax):
                curx += dirx
                cury += diry
                # path.append((dist, dist + 1))
                dist += 1
                # print(curx)
                # print(cury)
                grid[curx - 1][cury - 1] = dist
                if dist - 1 + abs(curx - mid) + abs(cury - mid) == k:
                    # new_path = add_direct_path(curx, cury, dirx, diry,mid, dist)
                    # path.extend(new_path)
                    sol_pos = (curx, cury)
                    # sol = path[:]
            if dirx == 1:
                ymin += 1
            if dirx == -1:
                ymax -= 1
            if diry == 1:
                xmax -= 1
            if diry == -1:
                xmin += 1
    return sol_pos, grid


def add_direct_path(curx,cury, dirx, diry, mid, last):
    new_path = []
    if dirx == 1 and curx <= mid:
        for i in range(mid-curx):
            last+=1
            new_path.append(last)
        curx = mid
        for i in range(mid-cury):
            last += 4 * (n-cury)-1
            new_path.append(last)
            cury += 1
        assert cury == mid
    if dirx == 1 and curx > mid:
        pass

    return new_path


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        n, k = [int(x) for x in input().split(" ")]
        res = solve(n, k)
        if res == "IMPOSSIBLE":
            print("Case #{i}: {res}".format(i=t, res=res), flush=True)
        else:
            print("Case #{i}: {res}".format(i=t, res=len(res)), flush=True)
            for x, y in res:
                print(f"{x} {y}")

