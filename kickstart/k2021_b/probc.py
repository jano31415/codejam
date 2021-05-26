import math

def solve(Z):
    if Z <= 1000:
        return slow_solve(Z)
    psq = int(math.sqrt(Z))+1
    range_p = 1000
    poss_p = [i+psq for i in range(-range_p, range_p)]
    for i in range(2, int(2*math.sqrt(psq))):
        for j in range(1, range_p//i + 3):
            index = range_p - psq%i + j*i
            if 0 <= index < len(poss_p):
                poss_p[index] = 0
            index = range_p - psq%i - (j-1)*i
            if 0 <= index < len(poss_p):
                poss_p[index] = 0
    big_p = []
    for i in range(1,range_p):
        if poss_p[range_p+i] != 0:
            b_p = poss_p[range_p+i]
            big_p.append(b_p)
    small_p = []
    for i in range(range_p):
        if poss_p[range_p-i] != 0:
            s_p = poss_p[range_p-i]
            small_p.append(s_p)

    # print(big_p)
    # print(small_p)

    if small_p[0] * big_p[0] <= Z:
        return small_p[0] * big_p[0]
    if small_p[1] * small_p[0] <= Z:
        return small_p[1] * small_p[0]

    return small_p[1] * small_p[2]


def slow_solve(Z):
    psq = int(math.sqrt(Z))+1
    primes = []
    for i in range(2,psq+50):
        if slow_test_prime(i):
            primes.append(i)
    primes = primes[::-1]
    for i,x in enumerate(primes):
        if primes[i]*primes[i+1] <= Z:
            return primes[i]*primes[i+1]


def slow_test_prime(p):
    for i in range(2,p):
        if p%i == 0:
            return False
    return True


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
    T = int(input())
    sol = []
    for t in range(1, T+1):
        Z = int(input())
        res = solve(Z)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        sol.append(res)

    # for t in range(1, T + 1):
    #     should_be = input()
    #     should_be = int(should_be.split(":")[1][1:])
    #     if should_be != sol[t-1]:
    #         print(t)

# import time
# a=time.time()
# print(solve(10**18, primes))
# b=time.time()
# print(b-a)
# print(slow_solve(100100))
# print(solve(3600, primes))
# print(solve(3598,primes))
# print(solve(10**18))
