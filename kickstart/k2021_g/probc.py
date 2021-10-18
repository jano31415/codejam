def solve(n,k,bananas):
    tot = 0
    cumsum = [0]*(n+1)
    for i,b in enumerate(bananas):
        if b==k:
            return 1
        tot+=b
        cumsum[i+1] = tot

    if cumsum[-1] < k:
        return -1

    sum_dict = {}
    for i in range(n):
        for j in range(i+1, n+1):
            sum_val = cumsum[j] - cumsum[i]
            if sum_val not in sum_dict:
                sum_dict[sum_val] = []
            sum_dict[sum_val].append((i,j))

    for key in sum_dict:
        sum_dict[key].sort(key=lambda x: x[1]-x[0])
    best = n+1
    for interval1 in range(1,k):
        if interval1 not in sum_dict:
            continue
        for i1,j1 in sum_dict[interval1]:
            if k-interval1 not in sum_dict:
                break
            for i2,j2 in sum_dict[k-interval1]:
                if (j1 <= i2) or (j2 <= i1):
                    # print(i1, j1, i2, j2)
                    cur_sol = j1-i1 + j2-i2
                    if cur_sol < best:
                        best = cur_sol
    if best > n:
        best = -1
    return best



#
# if __name__ == "__main__":
#
#     T = int(input())
#     for t in range(1,T+1):
#         n,k = [int(x) for x in input().split(" ")]
#         bananas = [int(x) for x in input().split(" ")]
#         res = solve(n,k,bananas)
#         print("Case #{t}: {res}".format(t=t, res=res), flush=True)
import random
import time
n=1000
max_n = 10**6
k = random.randint(6*max_n, 12*max_n)
ban = [random.randint(0,max_n) for _ in range(n)]
a = time.time()
res=solve(n,k,ban)
b=time.time()
print(res)
print(b-a)