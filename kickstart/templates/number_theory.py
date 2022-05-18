def invert_mod(i, mod_val):
    return pow(i, mod_val-2, mod_val)


# n choose k mod mod_val . use cache
fac_cache = {}
inv_fac_cache = {}
mod_val = 10**9+7
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

# quick sieve of
def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend(3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1)
    return res
