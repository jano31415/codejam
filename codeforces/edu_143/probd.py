def solve(n,w):
    mod = 998244353
    dyn = {0:1}
    for i in range(len(w)//3):
        dyn2 = {}
        w1,w2,w3 = w[3*i], w[3*i+1], w[3*i+2]
        for wi in [w1,w2,w3]:
            if wi == min([w1,w2,w3]):
                for k in dyn.keys():
                    dyn2[k+wi] = (dyn2.get(k+wi,0) + dyn[k])%mod
        dyn=dyn2
    maxk = min(dyn.keys())
    return (dyn.get(maxk,0) * choose(n//3,n//6, mod))%mod


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

fac_cache = {}
inv_fac_cache = {}
mod_val = 998244353

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

def invert_mod(i, mod_val):
    return pow(i, mod_val-2, mod_val)


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n = int(input().decode().strip())
    w = [int(x) for x in input().decode().strip().split()]

    res = solve(n,w)
    print(res)