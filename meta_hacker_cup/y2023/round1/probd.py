

def solve(n,days,q,qlist):
    multi = 1000000006
    mod = 1000000007
    minus_days = [(d*multi)%mod for d in days]
    all_vals = [(days[i], -i-1, 1) for i in range(n)] + [(minus_days[i], -i-1, -1) for i in range(n)]
    all_vals.sort(reverse=True)
    qfound = [0]*q
    qsum=0
    total = 0
    for v, index, pm in all_vals:
        index = abs(index)
        plus_minus = 1
        for i, lr in enumerate(qlist):
            l,r=lr
            if l<= index <=r:
                plus_minus *= -1
                if pm == plus_minus and qfound[i] ==0:
                    qsum+=1
                    total+=index
                    qfound[i]=1
        if qsum==q:
            return total
    return total



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_c.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        n = int(input().decode().strip())
        days = [int(x) for x in input().decode().strip().split(" ")]
        q = int(input().decode().strip())
        qlist = [0]*q
        for i in range(q):
            l,r=[int(x) for x in input().decode().strip().split(" ")]
            qlist[i] = (l,r)
        print(f"n {n}, q {q}")
        res1=solve(n,days,q,qlist)
        print(res1)
        with open("out_c.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")


