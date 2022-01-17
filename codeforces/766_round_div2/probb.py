def solve(n,m):
    if n < m:
        tmp = n
        n = m
        m = tmp
    sol=[]
    if n %2 == 0:
        first_mult = 2
    else:
        first_mult = 1
    if m%2 == 0:
        top = 2
    else:
        top = 1
    sum = 0
    tot = first_mult*top + 2*sum
    min_walk = n//2 + m//2
    tot_old=0
    bot=0
    while True:
        new_seats = tot-tot_old
        if len(sol) == (n * m):
            return sol
        for x in range(new_seats):
            sol.append(str(min_walk))
            if len(sol) == (n*m):
                return sol
        sum += top -bot
        top = min(top+2, n)
        if top >= m:
            if bot == 0:
                bot = n%2
            else:
                bot += 2

        min_walk+=1
        tot_old = tot
        tot = first_mult * top + 2 * sum
    return sol

def solve2(n,m):
    if m%2 == 1:
        tmp = n
        n=m
        m=tmp
    if n%2 ==0 and m%2==0:
        start=4
    elif n%2==1 and m%2==0:
        start=2
    else:
        start=1
    top= 1 if n%2==1 else 2
    sol=[]
    count = 2 if (n*m)%2==0 else 1
    start_count = count
    min_walk = n//2 + m//2
    first=0
    while True:

        if len(sol) == n * m:
            return sol
        for i in range(start):
            if len(sol) == n*m:
                return sol
            sol.append(str(min_walk))
        min_walk+=1
        if start == 1:
            start-=1
        if count < min(n,m):
            start += 4
        elif count >= min(n,m) and count < max(n,m):
            start = 2*min(n,m)
        else:
            if first == 0:
                first = 2 if min(n,m)%2 == 0 else 1
            start = 2*(min(n,m) - first)
            first+=2
        count+=2





import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split()]
        res=solve2(n,m)
        res = " ".join(res)
        print(res, flush=True)
