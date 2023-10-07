# turn every kth button, sort Q, if numbers double skip,
# start with the smallest to flip and flip greedily
import random
import time

def solve(n,s,q,qlist):
    # simulate q
    a=time.time()
    if n>10**4 or q>10**4:
        print(f"big n {n} q {q}")
    qlist.sort()
    d = {}
    for x in qlist:
        if x not in d:
            d[x] = 0
        d[x] += 1
    for x in d:
        d[x] = d[x]%2
    keys = [x for x in d if d[x]!=0]
    for x in keys:
        simulate_si(s,x)
    # simulation end
    count=0
    for i,si in enumerate(s):
        if si == 1:
            simulate_si(s, i+1)
            count+=1
    print(time.time()-a)
    return count

def simulate_si(s, x):
    for m in range(1, n // x + 1):
        ind = m * x - 1
        # if ind < n:
        s[ind] = (s[ind] + 1) % 2
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_c.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        n = int(input().decode().strip())
        s = [int(x) for x in input().decode().strip()]
        q = int(input().decode().strip())
        qlist = [0]*q
        for i in range(q):
            qlist[i]=int(input().decode().strip())

        res1=solve(n,s,q,qlist)
        print(res1)
        with open("out_c.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")

def run_big(n):
    s= [random.randint(0,1)]*n
    qlist = [random.randint(1,n) for I in range(n)]
    solve(n,s,n,qlist)
# run_big(4*10**6)