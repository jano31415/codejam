def solve(n,a,b,king):
    lastx=0
    capital = 0
    cost=0
    for i,xi in enumerate(king):
        conq_cost = b * (xi - capital)
        # print(f"cost conquer {conq_cost}")
        cost += conq_cost
        if (n-i-1)*b* (xi-capital) > a*(xi-capital):
            # print(f"move to {xi}")
            cost += a*(xi-capital)
            capital = xi
    return cost

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,a,b = [int(x) for x in input().decode().strip().split()]
        king = [int(x) for x in input().decode().strip().split()]

        res=solve(n,a,b, king)
        print(res)
