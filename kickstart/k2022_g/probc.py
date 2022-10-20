def solve(n, arr):
    prefix = [0]*(n+1)
    cur=0
    for i,x in enumerate(arr):
        prefix[i] = cur
        cur+=x
    prefix[-1] = cur
    # print(prefix)
    # tot = 0
    # for l in range(n):
    #     for r in range(l,n):
    #         cur = prefix[r+1] - prefix[l]
    #         if cur>0:
    #             print(cur)
    #             print(l,r)
    #             tot+=cur
    tot=0
    l=0
    min_cur = 10**9
    for r in range(n):
        cur = prefix[r + 1] - prefix[l]
        if cur < min_cur:
            min_cur = cur
        if cur < 0:
            l_last = l
            for l in range(l_last, r):
                min_cur -= arr[l]
                if min_cur >= 0:
                    tot += prefix[r + 1] - prefix[l]
            min_cur = 10 ** 9
            l=r+1
        else:
            tot+=cur
    l_last = l
    for l in range(l_last, n):
        min_cur -= arr[l]
        if min_cur >= 0:
            tot += prefix[n] - prefix[l+1]
    # tot+=cur
    return tot

def solve_n2(n,arr):
    prefix = [0] * (n + 1)
    cur = 0
    for i, x in enumerate(arr):
        prefix[i] = cur
        cur += x
    prefix[-1] = cur
    tot = 0
    for l in range(n):
        for r in range(l, n):
            cur = prefix[r + 1] - prefix[l]
            if cur < 0:
                break
            else:
                tot += cur
    return tot


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        arr = [int(x) for x in input().split()]
        res = solve(n, arr)
        print("Case #{t}: {res}".format(t=t,
            res=res), flush=True)

import random
n=8
for i in range(20):
    arr = [random.randint(-10,10) for _ in range(n)]
    res1 = solve(n, arr)
    res2 = solve_n2(n,arr)
    if res1 != res2:
        print(" ".join([str(x) for x in arr]))
        print(res1)
        print(res2)
        break
