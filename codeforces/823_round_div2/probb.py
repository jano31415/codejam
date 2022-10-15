def solve(n,orbits, waiting):
    pos_time = [(orbits[i], waiting[i]) for i in range(n)]
    pos_time.sort()
    l = pos_time[0][0]
    r = pos_time[-1][0]
    max_t = max(waiting)
    # only pos would be (r+l)/2
    mid= (r+l)/2
    comb = []
    for i in range(n):
        pos,time = pos_time[i]
        if pos > mid:
            new_pos = pos + time
        else:
            new_pos = pos - time
        # comb.append((new_pos, pos,time))
        comb.append((pos + time, pos,time))
        comb.append((pos - time, pos,time))


        # comb[i] = new_pos,po
    comb.sort()

    res= (comb[-1][0] + comb[0][0])/2
    if res < comb[0][1]:
        res = comb[0][1]
    if res > comb[-1][1]:
        res = comb[-1][1]
    return res


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        orbits = [int(x) for x in input().decode().strip().split()]
        waiting = [int(x) for x in input().decode().strip().split()]

        res=solve(n,orbits, waiting)
        print(res)

