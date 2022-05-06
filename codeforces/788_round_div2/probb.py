import math
def solve(n, s, forbidden):
    forbidden = set(forbidden)
    indexes = [0]
    for i, x in enumerate(s):
        if x in forbidden:
            indexes.append(i)
    if len(indexes)==1:
        return 0
    maxi = max(indexes)
    diff_index = []
    for i in range(len(indexes)-1):
        diff_index.append(indexes[i+1] - indexes[i])
    return max(diff_index)
    # this part is not needed too complicated
    # tot = 0
    # counts = {}
    # for x in diff_index:
    #     counts[x] = counts.get(x, 0)+1
    # remain = len(indexes)-1
    # if s[0] in forbidden:
    #     remain -=1
    # if maxi == 0:
    #     return 0
    # for i in range(1, max(diff_index)+2):
    #     tot += remain
    #     remain -= counts.get(i, 0)
    #     if tot >= maxi:
    #         return i
    # return i



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()
        forbidden = [x for x in input().decode().strip().split()]
        lenf = forbidden.pop(0)
        assert int(lenf) == len(forbidden)
        res=solve(n, s, forbidden)
        print(res)

