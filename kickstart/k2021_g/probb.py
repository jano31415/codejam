def solve(furniture):


    furny = [(a[1],a[3]) for a in furniture]
    furnx = [(a[0],a[2]) for a in furniture]

    xsol = get_x_sol(furnx)
    ysol = get_x_sol(furny)

    return f"{xsol} {ysol}"


def get_x_sol(furnx):
    # furnx.sort(key=lambda x: x[0] * 10**10 + x[1])
    # median point
    # mid = (len(furnx)-1) // 2
    cur = furnx[0][0]
    left = 0
    right = len(furnx)
    plus_minus = []
    for i, x in enumerate(furnx):
        x1, x2 = x
        # if x1 > cur:
        #     right += 1
        # elif x2 <= cur:
        #     left += 1
        plus_minus.append((x1, i, 1))
        plus_minus.append((x2, i, -1))
    plus_minus.sort(key=lambda x: x[0])
    tot = 0
    xsol = cur
    for x, i, pl_mi in plus_minus:
        # if x <= cur:
        #     continue
        if (left - right) >= 0:
            xsol = cur
            break
        else:
            cur = x
            if pl_mi == 1:
                right -= 1
            if pl_mi == -1:
                left += 1
    return xsol


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        k = int(input())
        furniture = []
        for i in range(k):
            #bottom left, and top right
            xi1, yi1, xi2, yi2 = [int(x) for x in input().split(" ")]
            furniture.append((xi1,yi1, xi2, yi2))

        res = solve(furniture)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)