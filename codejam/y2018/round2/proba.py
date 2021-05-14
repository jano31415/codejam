def solve(C, col_nr):
    imposs_str = "IMPOSSIBLE"
    if sum(col_nr) != C:
        return imposs_str
    sol = []
    start_pos = [1]*C
    left_needed = 0
    try:
        while True:
            left_needed = 0
            next_pos = start_pos[:]
            row_sol = []
            for i,x in enumerate(start_pos):
                left_needed = sum(col_nr[:i]) - sum(start_pos[:i])
                right_needed = sum(col_nr[i+1:]) - sum(start_pos[i+1:])
                if (left_needed > 0) and (right_needed > 0):
                    raise ValueError("IMPOSSIBLE")
                # if we have too much throw right.
                if left_needed>0:
                    put_left(i, row_sol, start_pos, next_pos)
                elif right_needed>0:
                    put_right(i, row_sol, start_pos, next_pos)
                else:
                    row_sol.append(".")
                # if x > col_nr[i]:
                #     if left_needed > 0:
                #         put_left(i, row_sol, start_pos, next_pos)
                #         left_needed -= x
                #     else:
                #         put_right(i, row_sol, start_pos, next_pos)
                # elif x < col_nr[i]:
                #     left_needed = col_nr[i] - x
                #     row_sol.append(".")
                # else:
                #     row_sol.append(".")
            if len(sol) > 1000:
                break
            sol.append(row_sol)
            start_pos = next_pos[:]
            if row_sol == ["."]*C:
                break
    except Exception:
        return "IMPOSSIBLE"
    return sol

def put_left(i, sol, curr_pos, next_pos):
    if i in [0, len(curr_pos)-1]:
        raise ValueError("tried left on the left")
    next_pos[i] -= curr_pos[i]
    next_pos[i-1] += curr_pos[i]
    sol.append("/")


def put_right(i, sol, curr_pos, next_pos):
    if i in [0, len(curr_pos)-1]:
        raise ValueError("tried left on the left")
    next_pos[i] -= curr_pos[i]
    next_pos[i+1] += curr_pos[i]
    sol.append("\\")


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        C = int(input())
        col_nr = [int(x) for x in input().split(" ")]
        res = solve(C, col_nr)
        if res == "IMPOSSIBLE":
            print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        else:
            print("Case #{t}: {res}".format(t=t, res=len(res)), flush=True)
            for sol in res:
                print("{res}".format(t=t, res="".join(sol)), flush=True)

