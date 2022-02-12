import random
def solve2(n,m, arr, pairs):
    pairs = set(pairs)
    arr.sort()
    counts = dict()
    for a in arr:
        if a not in counts:
            counts[a] = 0
        counts[a] += 1
    count_list = []
    for k in counts:
        count_list.append((counts[k],k))

    count_sort = sorted(count_list, key=lambda x: -x[0])
    val_sort = sorted(count_list, key=lambda x: -x[1])
    len_tup = len(count_sort)
    best_val = 0
    best_tup = ()
    for i in range(min(len_tup, 3000)):
        for j in range(min(len_tup, 3000)):
            counta, a = count_sort[i]
            countb, b = val_sort[i]
            if a == b:
                continue
            if (b, a) in pairs:
                continue
            if (a, b) in pairs:
                continue
            new_val = (counta+countb) * (a+b)
            if new_val > best_val:
                best_tup = ((counta,a),(countb, b))
                best_val = new_val
    # print(best_tup)
    ((counta, a), (countb, b)) = best_tup
    tuplist = [(countx,x) for countx,x in val_sort if (countx > min(counta,countb) or x > min(a,b))]
    for i in range(len(tuplist)):
        for j in range(len(tuplist)):
            counta, a = tuplist[i]
            countb, b = tuplist[i]
            if a == b:
                continue
            if (b, a) in pairs:
                continue
            if (a, b) in pairs:
                continue
            new_val = (counta+countb) * (a+b)
            if new_val > best_val:
                best_val = new_val

    return best_val


def solve(n,m, arr, pairs):
    pairs = set(pairs)

    counts = dict()
    for a in arr:
        if a not in counts:
            counts[a] = 0
        counts[a] += 1

    count_to_val = {}
    for k in counts:
        if counts[k] not in count_to_val:
            count_to_val[counts[k]] = []
        count_to_val[counts[k]].append(k)

    for k in count_to_val:
        count_to_val[k].sort(reverse=True)

    best_val = 0
    for a in counts:
        counta = counts[a]
        for k in count_to_val:
            candidates = count_to_val[k]
            for c in candidates:
                if a == c:
                    continue
                if (a, c) in pairs or (c, a) in pairs:
                    continue
                new_val = (counta + k) * (c+a)

                if new_val > best_val:
                    best_val = new_val
                break
    return best_val

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split(" ")]
        arr = [int(x) for x in input().decode().strip().split(" ")]
        pairs = []
        for j in range(m):
            a,b = [int(x) for x in input().decode().strip().split(" ")]
            pairs.append((a,b))
        res1 = solve(n,m, arr, pairs)
        print(res1)
        # print("\n")