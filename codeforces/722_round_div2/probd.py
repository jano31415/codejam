import math
#took me way too long. didnt finish in contest.

def solve(N):
    mod_val = 998244353
    if N == 1:
        return 1
    dyn = [0]*(N + 1)
    dyn[2] = 1
    dyn[0] = 1
    dyn2 = sieve2(N+1)
    for n2 in range(4, N+1, 2):
        dyn[n2] = (2*dyn[n2-2] + dyn2[n2] - dyn2[n2-2]) % mod_val
    return dyn[N]

def get_even_div_primes(n2, primes):
    l=[]
    if n2 in primes:
        return 2
    for p in primes:
        cur = 0
        while n2 % p == 0:
            cur += 1
            n2 = n2//p
        if cur > 0:
            l.append(cur)
        if (n2 == 1) or (n2 in primes):
            break
    tot = 1
    for x in l:
        tot = tot * (x+1)
    return tot

def get_even_div(mod_val, n2):
    new_dyn = (1 - (n2 % 2))
    for i in range(2, int(math.sqrt(n2)) + 1):
        if i ** 2 == n2:
            new_dyn = (new_dyn + (1 - (i % 2))) % mod_val
        elif n2 % i == 0:
            one_two = (1 - i % 2) + (1 - (n2 // i) % 2)
            # if i%2 == 0:
            #     print(f"{n2} all same {i}")
            # if (n2//i) %2 == 0:
            #     print(f"{n2} all same {n2//i}")

            new_dyn = (new_dyn + one_two) % mod_val
    return new_dyn

def sieve2(max_p):
    div_count = [0]*(max_p+1)
    for i in range(2, max_p,2):
        for j in range(1, max_p//i + 1):
            div_count[i*j] += 1
    return div_count
# sieve of the eratosthenes
def sieve(max_p):
    primes = [2, 3]
    for i in range(5,max_p):
        is_prime=True
        for p in primes:
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

if __name__ == "__main__":
    N = int(input())
    # import time
    # a = time.time()
    res = solve(2*N)
    # b=time.time()
    # print(b-a)
    print(res, flush=True)