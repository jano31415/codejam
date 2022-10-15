def solve(s):
    sint = [int(x) for x in s]
    count0 =0
    n=len(s)
    last0=0
    for i,x in enumerate(sint):
        if x == 0:
            count0+=1
            last0 = i
    counts = [0]*10
    counts[0]=count0
    for nr in range(1,10):
        for i in range(last0,n):
            if sint[i] == nr:
                last0 = i
                counts[nr] += 1
    counts_shift = [0]*10
    for i,x in enumerate(sint):
        counts_shift[x]+=1
    counts_tot = [0]*10

    for i,x in enumerate(counts_shift):
        if i == 0:
            counts_tot[i]=counts[i]
        else:
            counts_tot[i] = counts[i] + max(0,counts_shift[i-1] - counts[i-1])
    # assert sum(counts_tot) == n
    res = []
    for i in range(10):
        res.append(str(i)*counts_tot[i])

    res= "".join(res)
    if len(res) != n:
        res = res + "9" * (n - len(res))
    return res


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        s = input().decode().strip()
        res=solve(s)
        print(res)

