def solve(a,b,c, primes):
    if c == 1:
        if a==b:
            return "NO"
        if (a%b == 0) or (b%a == 0):
            return "YES"
        else:
            return "NO"
    max_val = find_max(a,b, primes)
    if max_val>=c:
        return "YES"
    return "NO"

def find_max(a,b, primes):
    return find_max_one(a, primes) + find_max_one(b, primes)

def find_max_one(a,primes):
    if a == 1:
        return 0
    tot=0
    for p in primes:
        if a%p == 0:
            while a%p == 0:
                tot+=1
                a= a//p
        if a == 1:
            return tot
    # print("buggy")
    return tot+1


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
import math
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    primes = sieve(int(math.sqrt(10**9 + 10))+1)
    for t in range(T):
        a,b,c = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(a,b,c, primes)
        print(res)