def solve(R, B):
    dyn = {r: {b: set() for b in range(B+1)} for r in range(R+1)}
    dyn[0][0] = set([frozenset()])
    for r in range(R+1):
        for b in range(B+1):
            best_sol_len = 0
            for i in range(r+1):
                for j in range(b+1):
                    if i+j == 0:
                        continue
                    if len(dyn[r-i][b-j]) == 0:
                        print("no old solution found")
                    for old_sol in dyn[r-i][b-j]:
                        if (i, j) not in old_sol:
                            old_sol_new = old_sol.copy()
                            new_sol = old_sol_new.union(set([(i,j)]))
                            if len(new_sol) > best_sol_len:
                                best_sol_len = len(new_sol)
                                dyn[r][b].add(new_sol)
            dyn[r][b] = {x for x in dyn[r][b] if len(x) == best_sol_len}
    return dyn


def solve2(R):
    depth = 33
    dyn = [[set() for b in range(r+depth+2)] for r in range(R+1)]
    dyn[0][0] = set()
    for r in range(R+1):
        for b in range(r+1):
            best_sol_len = 0
            base_sol_len = 0
            if (r > 0) and (b>0):
                base_sol_len = max(len(dyn[r][b - 1]), len(dyn[r-1][b]))
                best_sol_len = base_sol_len-1
            break_i = False
            for j in range(min(b + 1, depth)):
                if break_i:
                    break
                for i in range(min(r+1, depth)):
                    old_sol = dyn[r-i][b-j]
                    if len(old_sol)+1 > best_sol_len:
                        if (i, j) not in old_sol:
                            new_sol = old_sol.copy()
                            new_sol.add((i, j))
                            best_sol_len = len(new_sol)
                            dyn[r][b] = new_sol
                            if base_sol_len > 0:
                                if best_sol_len == (base_sol_len+1):
                                    break_i = True
                                    break
                    elif len(old_sol) < best_sol_len-1:
                        break

    return dyn


import time
if __name__ == "__main__":
    T = int(input())
    # a = time.time()
    dyn = solve2(500)
    # b = time.time()
    # print(b-a)

    for t in range(1, T+1):
        R, B = [int(x) for x in input().split(" ")]
        if R >= B:
            # i honestly dont know why minus 1 but it does not work else
            print("Case #{t}: {res}".format(t=t, res=len(dyn[R][B])-1), flush=True)
        else:
            print("Case #{t}: {res}".format(t=t, res=len(dyn[B][R])-1), flush=True)
