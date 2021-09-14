#upsolve
def solve(n,m,sight):
    sight_i = [(-sight[i], i+1) for i in range(len(sight))]
    sight_i.sort(reverse=True)


    last_change = 0
    last_x = sight_i[0][0]
    new_order = []
    tmp = []
    for i,x in enumerate(sight_i):

        s,id = x
        if s != last_x:
            new_order = add_sights(last_change, m, new_order, tmp)
            last_change = i
            tmp=[]
        last_x = s
        tmp.append((s,id))

    last_change = add_sights(last_change, m, new_order, tmp)
    # print(new_order)


    order = [(j,new_order[j][1]) for j in range(len(sight))]
    # order.sort()

    # count inversions for each row.
    tot = 0
    for index,i in order:
        count = 0
        for k in range(1,m):
            if (index+k)%m <= index%m:
                break
            if order[index+k][1] > i:
                count+=1
        tot += count
    return tot


def add_sights(last_change, m, new_order, tmp):
    if last_change%m + len(tmp) < m:
        new_order += tmp
        return new_order

    first_split = m - last_change%m
    new_order += tmp[-first_split:]
    tmp = tmp[:-first_split]
    if len(tmp) > m:
        take_first = tmp[:len(tmp)%m]
        tmp = tmp[len(tmp)%m:]
        new_order += tmp
        new_order += take_first
    else:
        new_order += tmp
    return new_order


import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split(" ")]
        sight = [int(x) for x in input().decode().strip().split(" ")]

        res = solve(n,m,sight)
        print(res)

