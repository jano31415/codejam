def solve(n,k,s):
    if k == 0:
        return s, " ".join(["0" for a in range(n)])
    sol1 = []
    sol2 = []
    opp = {"1":"0", "0":"1"}
    if k %2 == 0:
        count = 0
        for si in s:
            if count == k:
                sol1.append(si)
                sol2.append(0)
            elif si == "0":
                sol1.append("1")
                sol2.append(1)
                count+=1
            else:
                sol1.append("1")
                sol2.append(0)
    else:
        count = 0
        for si in s:
            if count == k:
                sol1.append(opp[si])
                sol2.append(0)
            elif si == "1":
                sol1.append("1")
                sol2.append(1)
                count+=1
            else:
                sol1.append("1")
                sol2.append(0)

    count = sum(sol2)
    if count < k:
        if (k-count)%2 == 1:
            if sol1[-1] == "1":
                sol1[-1] = "0"
            else:
                sol1[-1] = "1"
        sol2[-1] += (k-count)
    return "".join(sol1), " ".join([str(x) for x in sol2])

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]
        s=input().decode().strip()

        res1,res2=solve(n, k, s)
        print(res1)
        print(res2)
