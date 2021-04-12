def solve_old(M, primes):
    primes_all = []
    for p,n in primes:
        for j in range(n):
            primes_all.append(p)
    return solve_recursive(M, primes_all, [], set())


def solve_recursive(M, primes, mult_grp, cache):
    mult = 1
    current = 0
    sum_primes = sum(primes)
    if len(mult_grp) == 0:
        current = 0
    else:
        for p in mult_grp:
            mult *= p
        if sum(primes) == mult:
            current = mult

    sols = [current]
    for i,p in enumerate(primes):
        mult_new = p*mult
        if mult_new <= sum_primes-p:
            primes_1 = primes[:i] + primes[i+1:]
            mult_new = mult_grp[:]
            mult_new.append(p)
            mult_set = [f"{x}_{mult_new.count(x)}" for x in mult_new]
            mult_set = frozenset(mult_set)
            if mult_set not in cache:
                cache.add(mult_set)
                res = solve_recursive(M, primes_1, mult_new, cache)
                sols.append(res)
    return max(sols)

def list_primes(n=500):
    primes = []
    for i in range(2,n):
        prime = True
        for p in primes:
            if i%p == 0:
                prime = False
        if prime:
            primes.append(i)
    if n == 500:
        assert len(primes) == 95
    return primes

def solve(M, primes):
    prime_dict = {}
    for p,n in primes:
        prime_dict[p] = n
    real_primes = list_primes(500)
    tot = sum_prime(primes)
    primes.sort(reverse=True)
    sum_biggest = 0
    prod = 1
    for p,n in primes:
        for i in range(n):
            if prod > tot:
                break
            prod *= p
            sum_biggest += p
        if prod > tot:
            break
    for i in range(sum_biggest):
        curr = tot - i
        this_primes = get_primes(curr, real_primes)
        if len(this_primes) == 0:
            continue
        if i == sum(this_primes):
            enough_primes = True
            for p in this_primes:
                if this_primes.count(p) > prime_dict.get(p, 0):
                    enough_primes = False
            if enough_primes:
                return curr
    return 0

def get_primes(p, real_primes):
    this_primes = []
    while p != 1:
        run_again = False
        for q in real_primes:
            if p % q == 0:
                p = p //q
                this_primes.append(q)
                run_again = True
                break
        if not run_again:
            return []
    return this_primes

def sum_prime(primes):
    tot = 0
    for p,n in primes:
        tot += p *n
    return tot

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        M = int(input())
        primes = []
        for i in range(M):
            P, N = [int(x) for x in input().split(" ")]
            primes.append((P,N))
        assert len(primes) == M
        # import time
        # a = time.time()
        res = solve(M, primes)
        # b = time.time()
        # print(b-a)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)