import math
import random


def solve(n,x):
    if len(str(x)) > n:
        if "0" in str(x):
            if n == 1:
                return 1
        return -1
    maxdig = max([int(a) for a in str(x)])
    if maxdig == 1:
        return -1
    dp = [set() for _ in range((2*n+1))]
    dp[0] = {x}
    for i in range(2*n):
        maxlen = max([len(str(a)) for a in dp[i]])
        if maxlen == n:
            return i
        for a in dp[i]:
            digs = set(str(a))
            for dig in digs:
                newa = int(dig) * a
                dp[i+1].add(newa)

    return -1
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,x = [int(x) for x in input().decode().strip().split()]
    res1= solve(n,x)
    print(res1)
