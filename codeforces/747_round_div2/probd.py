def solve(n,m, comments):
    neigh = [[] for _ in range(n+1)]
    for i,j,c in comments:
        neigh[i].append((j,c))
        neigh[j].append((i,c))
    comments = []
    smallest_unseen = 1
    i_map = [-1]*(n+2)
    opposite = {"c":"i", "i": "c"}
    tot = 0
    while smallest_unseen <= n:
        i_map = i_map
        i_map[smallest_unseen] = "i"
        i_count_imp = {"i": 1, "c": 0}

        res_imp, i_count, swap_index = traverse(i_map, neigh, opposite, smallest_unseen, i_count_imp)
        if res_imp == -1:
            return -1
        if (i_count["i"] < i_count["c"]):
            for index in swap_index:
                i_map[index] = opposite[i_map[index]]
            i_count["i"] = i_count["c"]
        tot += i_count["i"]
        for i in range(n):
            smallest_unseen+=1
            if i_map[smallest_unseen] == -1:
                break
    return tot


def traverse(i_map, neigh, opposite, smallest_unseen, i_count):
    known = [smallest_unseen]
    swap_index = [smallest_unseen]
    while len(known) > 0:
        cur = known.pop()
        for j, c in neigh[cur]:
            if i_map[cur] == "c":
                new_val = c
            else:
                new_val = opposite[c]
            if i_map[j] != -1 and i_map[j] != new_val:
                return -1, i_count, []
            else:
                if i_map[j] == new_val:
                    continue
                i_map[j] = new_val
                swap_index.append(j)
                i_count[new_val] += 1
                known.append(j)
    return 1, i_count, swap_index


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split(" ")]
        comments = []
        for _ in range(m):
            i, j, c = [x for x in input().decode().strip().split(" ")]
            comments.append((int(i), int(j), c[0]))


        resa = solve(n,m,comments)
        # check(res)
        print(resa)

