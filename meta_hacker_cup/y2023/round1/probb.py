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

def solve(P, sieve):
    prime_decomp= []
    for pi in sieve:
        if P%pi == 0:
            while P%pi == 0:
                P = P/pi
                prime_decomp.append(pi)
            if P == 1:
                break
    if P != 1:
        return -1
    s=41
    if sum(prime_decomp) == s:
        return prime_decomp
    if sum(prime_decomp) > 41:
        return -1
    if sum(prime_decomp) < 41:
        for i in range(41-sum(prime_decomp)):
            prime_decomp.append(1)
        return prime_decomp
        # merge some
        # l = [prime_decomp]
        # change=True
        # while change:
        #     change=False
        #     # print(len(l))
        #     for prime_decomp in l:
        #         old_sum = sum(prime_decomp)
        #         for i,pi in enumerate(prime_decomp):
        #             for j in range(i+1, len(prime_decomp)):
        #                 pj=prime_decomp[j]
        #                 if i<j:
        #                     new_sum = old_sum - pi -pj + pi*pj
        #                     if new_sum > 41:
        #                         continue
        #                     else:
        #                         new_prime_comp = prime_decomp[:]
        #                         new_prime_comp.remove(pi)
        #                         new_prime_comp.remove(pj)
        #                         new_prime_comp.append(pi*pj)
        #                         new_prime_comp.sort()
        #                         if new_sum == 41:
        #                             return new_prime_comp
        #                         else:
        #                             if new_prime_comp not in l:
        #                                 l.append(new_prime_comp)
        #                                 change=True



import math
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_b.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    sieve = prime_list(int(math.sqrt(10**9))+1)
    print(len(sieve))
    for t in range(1,T+1):
        P = int(input().decode().strip())
        res1=solve(P,sieve)
        if res1 != -1 and res1 is not None:
            assert sum(res1) == 41
            res1 = f'{str(len(res1))} {" ".join([str(x) for x in res1])}'
        print(res1)
        with open("out_b.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")
