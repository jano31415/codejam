def solve(grid, R, C, H, V):
    tot_chip = sum([sum(x) for x in grid])
    imposs_string = "IMPOSSIBLE"
    nr_per_piece = tot_chip // ((H+1)*(V+1))

    if tot_chip % ((H+1)*(V+1)) != 0:
        return imposs_string


    ### row checks
    row_sums = [sum(x) for x in grid]
    row = 0
    row_cuts = []
    pieces_H = nr_per_piece * (V+1)
    for h in range(H):
        choc_sum = 0
        for r in range(row, R):
            choc_sum += row_sums[r]
            if choc_sum > pieces_H:
                return imposs_string
            if choc_sum == pieces_H:
                row_cuts.append(r)
                row = r+1
                break
        if choc_sum < pieces_H:
            return imposs_string

    if H==0:
        last_row=0
    else:
        last_row=row_cuts[-1]+1

    last_row_sum = 0
    for x in range(last_row, R):
        last_row_sum += row_sums[x]
    if last_row_sum != pieces_H:
        return imposs_string

    all_row_cuts = [-1] + row_cuts + [R-1]
    col_sums = []
    for i in range(1, len(all_row_cuts)):
        col_sums.append(get_col_sum(all_row_cuts[i-1], all_row_cuts[i], grid))
    col=0
    col_cuts=[]
    for v in range(V):
        choc_sums = [0]*(len(row_cuts)+1)
        for c in range(col, C):
            for row_cut in range(len(all_row_cuts)-1):
                choc_sums[row_cut] += col_sums[row_cut][c]
            all_equal = True
            for choc in choc_sums:
                if choc > nr_per_piece:
                    return imposs_string
                if choc < nr_per_piece:
                    all_equal = False
                    break
            if all_equal:
                col_cuts.append(c)
                col = c+1
                break

    #col checks
    if V==0:
        last_row = 0
    else:
        last_row = col_cuts[-1]+1
    choc_sums = [0] * (len(row_cuts) + 1)
    for c in range(last_row, C):
        for row_cut in range(len(all_row_cuts) - 1):
            choc_sums[row_cut] += col_sums[row_cut][c]
    all_equal = True
    for choc in choc_sums:
        if choc > nr_per_piece:
            return imposs_string
        if choc < nr_per_piece:
            all_equal = False
            break
    if all_equal:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

def get_col_sum(i,j, grid):
    columns = [[row[c] for row in grid] for c in range(C)]
    col_sums = []
    for c in range(C):
        col_sums.append(sum(columns[c][i+1:j+1]))
    return col_sums


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        R, C, H, V = [int(x) for x in input().split(" ")]
        grid = []
        for r in range(R):
            row = [1 if x == "@" else 0 for x in input()]
            assert len(row) == C
            grid.append(row)
        assert len(grid) == R
        res = solve(grid, R, C, H, V)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)


