def solve(n,edges, primes):
    sol = [0]*(n-1)
    for i in range(1,n+1):
        if len(edges[i]) >2:
            return -1
        if len(edges[i]) == 1:
            start = i
    last_prime = 2
    last = None
    while True:
        this_edge = edges[start]
        this_edge = [x for x in this_edge if x[0] != last]
        if len(this_edge) == 0:
            break
        new_node, edge_id = this_edge[0]
        if last_prime ==2:
            last_prime =5
        elif last_prime ==5:
            last_prime =2
        sol[edge_id] = str(last_prime)
        last = start
        start = new_node
    return sol


def sieve(max_p):
    primes = [2, 3]
    for i in range(5, max_p):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    primes = sieve(10**4)
    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        edges={i:[] for i in range(1,n+1)}
        for i in range(n-1):
            u,v = [int(x) for x in input().decode().strip().split()]
            edges[u].append((v,i))
            edges[v].append((u,i))

        res=solve(n,edges, primes)
        if res != -1:
            res = " ".join(res)
        print(res, flush=True)
