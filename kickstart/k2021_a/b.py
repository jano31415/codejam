
def solve(R,C,grid):
    totl = 0
    rowl = [[0]*C for _ in range(R)]
    rowr = [[0]*C for _ in range(R)]

    for ri, row in enumerate(grid):
        rowr_tmp = 0
        for ci, c in enumerate(row):
            if c == 1:
                rowr_tmp +=1
            else:
                rowr_tmp = 0
            if rowr_tmp > 1:
                # initialize rowl as grid (saving some end of grid checks)
                # and then rowr_tmp is
                # rowl[ri][ci-1] so we dont need the tmp variable
                # if we dont use the tmp variable we can also fill
                # coll (top) by using coll[ri-1][ci]!
                rowl[ri][ci] = rowr_tmp

        rowr_tmp = 0
        for ci in reversed(range(C)):
            c = row[ci]
            if c == 1:
                rowr_tmp += 1
            else:
                rowr_tmp = 0
            if rowr_tmp > 1:
                rowr[ri][ci] = rowr_tmp

    coll = [[0] * C for _ in range(R)]
    colr = [[0] * C for _ in range(R)]
    for c in range(C):
        colr_tmp = 0
        for r in range(R):
            if grid[r][c] == 1:
                colr_tmp += 1
            else:
                colr_tmp = 0
            if colr_tmp > 1:
                coll[r][c] = colr_tmp
        colr_tmp = 0
        for r in reversed(range(R)):
            if grid[r][c] == 1:
                colr_tmp += 1
            else:
                colr_tmp = 0
            if colr_tmp > 1:
                colr[r][c] = colr_tmp

    for ri,row in enumerate(grid):
        for ci,c in enumerate(row):
            if c != 1:
                continue
            totl += get_l(rowl[ri][ci], coll[ri][ci])
            totl += get_l(rowr[ri][ci], coll[ri][ci])
            totl += get_l(rowr[ri][ci], colr[ri][ci])
            totl += get_l(rowl[ri][ci], colr[ri][ci])
    return totl

def get_l(a,b):
    if min(a,b) < 2:
        return 0
    # a is max: min(a//2, b) - 1, by symmetry:
    # we can micro optimize to .. -2
    return min(a//2, b) - 1 + min(a,b//2) - 1

def main():
    T = int(input())
    for t in range(1, T + 1):
        R, C = [int(x) for x in input().split(" ")]
        grid = []
        for r in range(R):
            row = [int(x) for x in input().split(" ")]
            assert len(row) == C
            grid.append(row)
        res = solve(R,C,grid)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)


main()