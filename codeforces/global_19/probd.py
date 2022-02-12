import random
def solve2(n, a, b):
    if n == 1:
        return 0
    suma = sum(a)
    sumb = sum(b)
    for _ in range(1000+100*n):
        i =random.randint(0,n-1)

        if a[i]*(suma - a[i]) + b[i]*(sumb - b[i]) > b[i]*(suma - a[i]) + a[i]*(sumb - b[i]):
            suma += (b[i]-a[i])
            sumb += (a[i]-b[i])
            tmp = a[i]
            a[i] = b[i]
            b[i] = tmp
    print(a)
    print(b)
    print(sum(a))
    print(sum(b))
    return cost(a) + cost(b)


def solve(n,a,b):
    if n==1:
        return 0
    dyn = [None]*(100*100 + 1)
    tot =0
    minarr =[]
    for i in range(n):
        mina= min(a[i],b[i])
        minarr.append(mina)
        tot += mina
    dyn[tot] = minarr
    exp = (sum(a)+sum(b))//2
    for i in range(tot, exp+1):
        cur = dyn[i]
        if cur is None:
            continue
        for j  in range(n):
            otherab = a[j] if a[j] != cur[j] else b[j]
            new_sum = i - cur[j] + otherab
            if dyn[new_sum] is None:
                new_list = cur[:]
                new_list[j] = otherab
                dyn[new_sum] = new_list

    for i in range(exp):
        if not dyn[exp-i] is None:
            soli = exp-i
            sol = dyn[soli]
            break
    other = a
    for j in range(n):
        otherab = a[j] if a[j] != sol[j] else b[j]
        other[j] = otherab
    return cost(sol) + cost(other)






def cost(a):
    tot=0
    for i in range(n):
        for j  in range(i+1,n):
            tot+= (a[i]+a[j])**2
    return tot

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a = [int(x) for x in input().decode().strip().split(" ")]
        b = [int(x) for x in input().decode().strip().split(" ")]
        res1 = solve(n, a, b)
        print(res1)
        # print("\n")