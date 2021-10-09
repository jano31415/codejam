def solve(n,c,s):
    l = []
    l2 = []
    for i,si in enumerate(s):
        if si != c:
            l.append(i+1)
        else:
            l2.append(i+1)
    if len(l) == 0:
        return 0, ""
    if len(l2) !=0:
        last = l2[-1]
        l =set(l)
        last_poss =True
        for i in range(2,n):
            if i*last in l:
                last_poss = False
                break
            if i*last > n:
                break
        if last_poss:
            return 1, last
    return 2,f"{n-1} {n}"




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,c = [x for x in input().decode().strip().split(" ")]
        s = input().decode().strip()

        resa,resb = solve(int(n),c,s)
        # check(res)
        print(resa)
        if resa >0:
            print(resb)
