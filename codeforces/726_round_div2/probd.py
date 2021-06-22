def solve_cache(N, primes):
    winloss = [0]*(N+1)
    for i in range(2, N+1):
        if i in primes:
            winloss[i]= 0
            continue
        for j in range(2,i):
            if i%j == 0:
                if winloss[i-j] == 0:
                    winloss[i] = 1
                    break
    return winloss

def solve(N, winloss):
    if winloss[N] == 1:
        return "ALICE"
    return "BOB"

def solve2(N):
    if N%2 == 1:
        return "Bob"
    count=0
    while N%2 == 0:
        N = N//2
        count+=1
    if N!=1:
        return "Alice"
    else:
        if count%2 == 0:
            return "Alice"
        else:
            return "Bob"

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

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        N = int(input().decode().strip())
        res = solve2(N)
        print(res)

# N = 10000
# primes = sieve(N)
# winloss = solve_cache(N, set(primes))
# for j in range(2,N):
#     res1=solve2(j)
#     print(res1)
#     res2=solve(j, winloss)
#     print(res2)
#     assert res1==res2
#     if j % 100 ==0:
#         print(j)