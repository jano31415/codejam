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

import math
def solve(n,arr, primes):
    # for each prime
    # count_wrong=0
    # for i,a1 in enumerate(arr):
    #     for j,a2 in enumerate(arr):
    #         if i<j and math.gcd(a1,a2)!=1:
    #             count_wrong+=1
    # if count_wrong == 0:
    #     return "YES"
    if len(set(arr)) < len(arr):
        return "NO"
    for p in primes:
        counts = {}
        for a in arr:
            if a%p not in counts:
                counts[a%p]=0
            counts[a%p]+=1
        if all([counts.get(c,0)>=2 for c in range(p)]):
            return "NO"
        # if len(set([a%p for a in arr])) == p:
        #     return "NO" 1 mod 2, 0 mod 3,3 mod 5,0 mod 7m0mod 11
    return "YES"
import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    primes = prime_list(10**3)
    for t in range(T):
        n = int(input().decode().strip())

        arr = [int(x) for x in input().decode().strip().split()]
        res=solve(n,arr, primes)
        print(res)
b=time.time()
# print(b-a)
#
# def solve_slow(arr):
#     for x in range(10000):
#         count_wrong=0
#         for i, a1 in enumerate(arr):
#             for j, a2 in enumerate(arr):
#                 if i < j and math.gcd(a1, a2) != 1:
#                     count_wrong+=1
#                     break
#             if count_wrong >0:
#                 break
#         if count_wrong == 0:
#             return "YES",x
#     return "NO",None
#
# import random
# solve(12,[40, 29, 94, 62, 64, 82, 74, 52, 44, 56, 86, 30],primes)
# n=12
# for i in range(1000):
#     arr = [random.randint(1,100) for _ in range(n)]
#     res1,x=solve_slow(arr)
#     res2 = solve(len(arr), arr, primes)
#     if res1!=res2:
#         print(arr)
#         print(x)
#
# def check(arr,x):
#     count_wrong=0
#     for i, a1 in enumerate(arr):
#         for j, a2 in enumerate(arr):
#             if i < j and math.gcd(a1+x, a2+x) != 1:
#                 print(a1,a2,math.gcd(a1+x,a2+x))
#                 count_wrong += 1
#                 break
#         if count_wrong > 0:
#             return False
#     return True
# print(check([40, 29, 94, 62, 64, 82, 74, 52, 44, 56, 86, 30], 693))
