def solve(n, wishes):
    wish_set = set(wishes)
    sol = len(wish_set)
    prio = -1
    if len(wish_set) == n-1:
        prio = [i for i in range(n) if i not in wish_set][0]
    seen = set()
    res_assignment = [-1]*n
    not_assigned = []
    if prio >= 0:
        res_assignment[prio] = wishes[prio]
        seen.add(wishes[prio])
    for i in range(n):
        if wishes[i] not in seen:
            res_assignment[i] = wishes[i]
            seen.add(wishes[i])
        else:
            if i != prio:
                res_assignment[i]=-1
                not_assigned.append(i)
    if len(not_assigned) == 1:
        res_assignment[not_assigned[0]] = prio
    else:
        not_gifted = [i for i in range(n) if i not in wish_set]
        not_assigned_set = set(not_assigned)
        not_gifted_same = [i for i in not_gifted if i in not_assigned_set]

        not_gifted_different = [i for i in not_gifted if
                                i not in not_assigned_set]
        not_gifted_same_set = set(not_gifted_same)
        not_assigned_different = [i for i in not_assigned if
                                  i not in not_gifted_same_set]
        assert len(not_assigned_different) == len(not_gifted_different)

        # assign same
        if len(not_gifted_same) != 1:
            for i in range(len(not_gifted_same)):
                res_assignment[not_gifted_same[i]] = not_gifted_same[(i+1) % len(not_gifted_same)]
        else:
            res_assignment[not_gifted_same[0]] = not_gifted_different[0]
            not_gifted_different[0] = not_gifted_same[0]

         # assign different
        for i in range(len(not_gifted_different)):
            res_assignment[not_assigned_different[i]] = not_gifted_different[i]
    return sol, " ".join([str(x+1) for x in res_assignment])





import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())

    for t in range(T):
        n = int(input().decode().strip())

        wishes=[int(x)-1 for x in input().decode().strip().split(" ")]
        res1, res2 = solve(n,wishes)
        print(res1)
        print(res2)