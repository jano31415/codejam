def solve(n,segments):
    min_l, max_r, c = segments[0]
    min_i, max_i = 0,0
    best_one =min_l, max_r, c

    for i in range(n):
        l,r,c = segments[i]
        if max_r < r:
            max_r = r
            max_i = i
        elif max_r ==r and (c < segments[max_i][2]):
            max_r = r
            max_i = i
        if min_l > l:
            min_l = l
            min_i = i
        elif min_l ==l and (c < segments[min_i][2]):
            min_l = l
            min_i = i
        onel,oner,onec = best_one
        if (l<onel and (r>=oner))or((l<=onel) and (r>oner)) or\
                (l==onel and r ==oner and c < onec):
            best_one = (l,r,c)

        tot=segments[min_i][2] + segments[max_i][2]
        onel,oner,onec = best_one
        if min_l == onel and max_r==oner:
            tot= min(tot, onec)
        print(tot)

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        segments = []
        for _ in range(n):
            l,r,c = [int(x) for x in input().decode().strip().split()]
            segments.append((l,r,c))
        res=solve(n,segments)
