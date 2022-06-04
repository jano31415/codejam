def solve(n,k,tokens):
    if k <= n:
        return solve_small_k(n,k,tokens)
    else:
        return big_k(n,k,tokens)

def big_k(n,k,tokens):
    already_there = sum(tokens)
    tot_fallen = k*n
    left = (n*(n+1))//2
    return already_there+tot_fallen-left

def simul(n,k):
    best_end_cur = 0
    best=0
    tmp={}
    for cur in range(n):
        snow = [0]*n
        dir = 1
        tot = 0
        # cur = 4
        for i in range(k):
            if cur == n-1:
                dir = -1
                # print(tot+snow[cur])
            elif cur == 0:
                dir = 1
                # print(tot+snow[cur])
            tot += snow[cur]
            # print(snow[cur])
            snow[cur]=0
            cur += dir
            snow = [x+1 for x in snow]
        tmp[cur]=tot
        if tot >= best:
            best = tot
            best_end_cur = cur
    print(f" best end cur {best_end_cur}")
    print(tmp)
    return tot

# for k in range(5, 23):
#     print(k)
#     print(f"simul {simul(7, k)}")
def solve_small_k(n,k,tokens):
    prefix = [0]* (n+1)
    cur = 0
    for i,x in enumerate(tokens):
        prefix[i] = cur
        cur += x
    prefix[-1] = cur
    best = 0
    for i in range(n+2):
        if i+k > n:
            break
        start_i = prefix[k+i] - prefix[i]
        if start_i > best:
            best = start_i
    best += (k * (k-1))//2
    return best


# check for each letter is it in? else can not be the start
#
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]
        tokens = [int(x) for x in input().decode().strip().split()]
        res=solve(n,k,tokens)
        print(res)

