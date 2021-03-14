# recursive first try, not efficient enough. See proba2
def solve(H,V, waffle, row_cuts, col_cuts, chocs_per_slice=None):
    # print(H)
    # print(V)
    if len(row_cuts) == 0 and len(col_cuts) ==0:
        chocs = sum(sum(waffle))
        # print(chocs)
        chocs_per_slice = chocs // ((H+1)*(V+1))
        if chocs == 0:
            raise SolutionFound()
        if chocs % (H+1)*(V+1) != 0:
            raise ImpossibleFound()

    if len(row_cuts) == H and len(col_cuts) == V:
        if check_sol(waffle, row_cuts, col_cuts, chocs_per_slice):
            raise SolutionFound()

    if len(row_cuts) != H:
        possible_rcut = find_row_cut(waffle, row_cuts, col_cuts, chocs_per_slice)

        for rcut in possible_rcut:
            solve(H, V, waffle, row_cuts + [rcut], col_cuts, chocs_per_slice)

    if len(col_cuts) != V:
        possible_ccut = find_col_cut(waffle, row_cuts, col_cuts, chocs_per_slice)

        for ccut in possible_ccut:
            solve(H, V, waffle, row_cuts, col_cuts + [ccut], chocs_per_slice)

    if len(row_cuts) == 0 and len(col_cuts) == 0:
        raise ImpossibleFound()

class SolutionFound(BaseException):
    def __init__(self):
        pass

class ImpossibleFound(BaseException):
    def __init__(self):
        pass

def find_row_cut(waffle, row_cuts, col_cuts, chocs_per_slice):
    possible_cuts = []
    for r in range(1,len(waffle)):
        if r in row_cuts:
            continue
        if check_sol_mod(waffle, row_cuts + [r], col_cuts, chocs_per_slice):
            possible_cuts.append(r)
    return possible_cuts

def get_pieces(waffle, row_cuts, col_cuts):
    row_cuts.sort()
    col_cuts.sort()
    row_cuts_tmp = row_cuts[:]
    col_cuts_tmp = col_cuts[:]

    row_cuts_tmp = [0] +row_cuts_tmp + [len(waffle)]
    col_cuts_tmp = [0] +col_cuts_tmp + [len(waffle[0])]

    pieces = []
    for rj in range(len(row_cuts_tmp)-1):
        for cj in range(len(col_cuts_tmp) - 1):
            r_start = row_cuts_tmp[rj]
            r_end = row_cuts_tmp[rj + 1]
            c_start = col_cuts_tmp[cj]
            c_end = col_cuts_tmp[cj + 1]

            tmp_sum = sum(sum(waffle[r_start:r_end, c_start:c_end]))
            pieces.append(tmp_sum)
    assert len(pieces) == (len(row_cuts)+1) * (len(col_cuts)+1)
    return pieces

def get_new_pieces_r(row_cuts, col_cuts, waffle, r):
    row_cuts_tmp = row_cuts[:]

    row_cuts_tmp = [0] + row_cuts_tmp + [len(waffle)]
    for rj in range(len(row_cuts_tmp) - 1):
        if row_cuts_tmp[rj] > r:
            row_cuts_tmp = [row_cuts_tmp[rj-1], r, row_cuts_tmp[rj]]


    tmp = [x for x in row_cuts if x > r]
    if len(tmp) == 0:
        row_cuts_tmp = [0,r,len(waffle)]
    col_cuts_tmp = col_cuts[:]

    row_cuts_tmp = [0] + row_cuts_tmp + [len(waffle)]
    col_cuts_tmp = [0] + col_cuts_tmp + [len(waffle[0])]

def check_sol(waffle, row_cuts, col_cuts, chocs_per_slice):
    a=time()
    pieces = get_pieces(waffle, row_cuts, col_cuts)
    b=time()
    # print(b-a)
    if all([x == chocs_per_slice for x in pieces]):
        return True
    return False

def check_sol_mod(waffle, row_cuts, col_cuts, chocs_per_slice):
    pieces = get_pieces(waffle, row_cuts, col_cuts)

    if all([x % chocs_per_slice ==0 for x in pieces]):
        return True
    return False

def find_col_cut(waffle, row_cuts, col_cuts, chocs_per_slice):
    possible_cuts = []
    for c in range(1,len(waffle[0])):
        if c in col_cuts:
            continue
        if check_sol_mod(waffle, row_cuts, col_cuts + [c], chocs_per_slice):
            possible_cuts.append(c)
    return possible_cuts

import numpy as np
T = int(input())
for i in range(1, T+1):
    R, C,H,V = [int(x) for x in input().split(" ")]
    waffle = []
    for j in range(R):
        waffle_row = [1 if x == "@" else 0 for x in input()]
        waffle.append(waffle_row)
    res = ""
    waffle = np.array(waffle)
    try:
        from time import time
        a = time()
        solve(H, V, waffle, [], [])

    except SolutionFound:
        res = "POSSIBLE"
    except ImpossibleFound:
        res = "IMPOSSIBLE"
        b = time()
        print(b - a)
    print("Case #{i}: {res}".format(i=i, res=res), flush=True)



def a():
    pass

def b():
    pass

def c():
    pass

# a()
# b()
# c()