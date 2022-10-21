def solve(n,m):
    mod = 998244353
    tot = 0
    primes = prime_list(n+1)
    pi = 0
    cur = 1
    old_ambig = m
    for i in range(2, n+1):
        tot = (tot + pow(m, i, mod)) %mod
        if pi < len(primes) and i == primes[pi]:
            cur *= primes[pi]
            pi+=1
        new_ambig = old_ambig * (m//cur)
        tot = (tot - new_ambig) % mod
        old_ambig = new_ambig
    return tot

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

# def sieve(max_p):
#     primes = [2, 3]
#     for i in range(5, max_p):
#         is_prime = True
#         for p in primes:
#             if i % p == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(i)
#     return primes


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,m = [int(x) for x in input().decode().strip().split()]

    res=solve(n,m)
    print(res)



#
# import time
# a=time.time()
# x=prime_list(3*10**5)
# print(time.time()-a)
#
#
# import time
# a=time.time()
# x=sieve(3*10**4)
# print(time.time()-a)