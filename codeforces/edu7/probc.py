def solve(n,tasks):
    mod_val = 998244353
    max1 = 0
    max2 = 0
    for t in tasks:
        if t > max1:
            max2 = max1
            max1 = t
        elif t > max2:
            max2 = t
    if max1 > max2 + 1:
        return 0
    if max1 == max2+1:
        count2 = tasks.count(max2)
        tot = get_factorial(n, mod_val)
        for i in range(n):
            if i >= count2:
                tmp = (choose(n-count2-1,i-count2, mod_val) *get_factorial(n-i-1, mod_val))%mod_val
                tmp = (tmp*get_factorial(i, mod_val))%mod_val
                tot = (tot - tmp)%mod_val
                # print(tot)
        return tot
    res = get_factorial(n, mod_val)

    # print(tasks)
    return res

fac_cache={}
inv_fac_cache = {}
mod_val = 998244353

def invert_mod(i, mod_val):
    return pow(i, mod_val-2, mod_val)

def choose(N,k, mod_val):
    if k == 0:
        return 1
    if k == N:
        return 1
    if k == 1:
        return N
    if k == (N-1):
        return N
    n_fac = get_factorial(N, mod_val)
    nk_inv_fac = get_inv_factorial(N-k, mod_val)
    k_inv_fac = get_inv_factorial(k, mod_val)
    res = (n_fac * nk_inv_fac) % mod_val
    res = (res * k_inv_fac) % mod_val
    return res

# if you run the biggest factorial first then all are cached
def get_factorial(N, mod_val):
    cached_res = fac_cache.get(N, None)
    if cached_res:
        return cached_res
    res = 1
    for i in range(2, N+1):
        res = (res * i) %mod_val
        fac_cache[i] = res
    return res


def get_inv_factorial(k, mod_val):
    cached_res = inv_fac_cache.get(k, None)
    if cached_res:
        return cached_res
    res = 1
    for i in range(2, k+1):
        res = (res * invert_mod(i, mod_val)) % mod_val
        inv_fac_cache[i] = res
    return res

import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        tasks = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,tasks)
        print(res)