def solve(n,m,s, queries):
    n1=n+1
    cache = {"abc":[0]*n1,
             "acb":[0]*n1,
             "bca": [0] * n1,
             "bac": [0] * n1,
             "cab": [0] * n1,
             "cba": [0] * n1
             }

    for i in range(n):
        for order in cache:
            change=0
            if order[i%3] != s[i]:
                change=1
            cache[order][i+1] = cache[order][i] + change

    for l,r in queries:
        best = n
        for order in cache:
            order_changes = cache[order][r] - cache[order][l-1]
            if order_changes < best:
                best = order_changes
        print(best)



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,m=[int(x) for x in input().decode().strip().split(" ")]
    s = input().decode().strip()
    queries = [0]*m
    for i in range(m):
        l,r=[int(x) for x in input().decode().strip().split(" ")]
        queries[i] =(l,r)
    solve(n,m,s,queries)
