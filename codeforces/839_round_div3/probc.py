def solve(k,n):
    l=[1]
    last=1
    diff=1
    for i in range(k-1):
        if last+diff <=n:
            last += diff
            diff+=1
            l.append(last)
    if len(l) < k:
        for i in range(n):
            if n-i not in l:
                l.append(n-i)
                if len(l) == k:
                    return sorted(l)
    else:
        return l
    raise ValueError()


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split()]
        res = solve(a,b)
        print(" ".join([str(x) for x in res]))
# import time
# a=time.time()
# n=10000
# solve(n=n, dep=[[]]+[set([i+2]) for i in range(n-1)]+[set()])
# b=time.time()
# print(b-a)