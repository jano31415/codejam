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


def find_smallest_prime(N, primes, first):
    for p in primes:
        if first and (p == 2):
            continue
        if N%p == 0:
            return p


def find_all_divisors(N):
    valid_div = []
    for p in range(2, min(N, 1000) + 1):
        if N % p == 0:
            valid_div.append(p)
    return valid_div

# first try, greedy doesnt work sometimes its not best to take smallest divisor
# need to try all of them, dynamic programming
def solve(N):
    N_orig = N
    count = 0
    sol = []
    first = True
    for i in range(10):
        if N == 1:
            sol[-1] = 2*sol[-1]
            break
        small_p = find_smallest_prime(N, primes, first)

        if not small_p:
            small_p = 4
        else:
            count+=1
        sol.append(small_p)
        N=N//small_p - 1
        if N ==0:
            break
        first = False
    new_sol = []
    cur = 1
    for p in sol:
        cur = cur*p
        new_sol.append(cur)
    assert sum(new_sol) == N_orig
    for i in range(len(new_sol)-1):
        if new_sol[i+1]%new_sol[i] != 0:
            raise ValueError("")
    return count

# try in competition. Memory overflow for test set 2.
# i had most of the thoughts needed. In the first idea i realized that we can
# just do N//p - 1 and ignore which p came before. Somehow when moving to
# dynamic programming i felt like i need to memorize also which product of primes
# we had used.
def solve_dyn(N):
    dyn = [{i:1} for i in range(0,N+1)]
    for x in range(3, N+1):
        miny=min(dyn[x].keys())
        if x+2*miny < N+1:
            for y in dyn[x]:
                for d in range(2, 1000):
                    if x+y*d > N:
                        break
                    dyn[x+y*d][y*d] = dyn[x][y]+1
        dyn[x] = max([dyn[x][y] for y in dyn[x]])
    return dyn

# after reading the analysis. When it works then it looks like the straightforward
# bottom up version from the first solution. :(
def solve_dyn2(N):
    dyn = [{"allow2":1, "dont2":1} for i in range(0,N+1)]
    dyn[2] = {"allow2":1, "dont2":0}
    dyn[0] = {"allow2":0, "dont2":0}
    dyn[1] = {"allow2":0, "dont2":0}

    for x in range(2, N+1):
        for d in range(2,N//(x+1) + 1):
            if d == 2:
                new_best = max(dyn[x]["dont2"], dyn[x]["allow2"]) + 1
                if dyn[2*(x+1)]["allow2"] < new_best:
                    dyn[2*(x+1)]["allow2"] = new_best
            else:
                new_best = dyn[x]["allow2"] + 1
                if dyn[d*(x+1)]["allow2"] < new_best:
                    dyn[d*(x+1)]["allow2"] = new_best
                if dyn[d*(x+1)]["dont2"] < new_best:
                    dyn[d*(x+1)]["dont2"] = new_best

    return dyn


if __name__ == "__main__":
    T = int(input())
    dyn = solve_dyn2(10**6+1)
    for t in range(1, T+1):
        N = int(input())
        res = dyn[N]["dont2"]
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)


import time
primes = sieve(1000)
N=10**4
dyn = solve_dyn(N+1)
dyn2 = solve_dyn2(N+1)
# checking memeory usage
print(len(str(dyn2)))

for i in range(3, 1001):
    res2 = dyn[i]
    res3 = dyn2[i]["dont2"]
    if res2 > res3:
        print(res2)
        print(res3)
        print("fail")
N=10**6
a=time.time()
dyn2 = solve_dyn2(N+1)
b=time.time()
print(b-a)