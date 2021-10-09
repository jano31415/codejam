def solve(n):

    mod = 10**9+7
    if n==1:
        return 6

    dp4 = [0] * (n+1)
    dp4[0] = 4
    for i in range(1, n):
        dp4[i] = (4*dp4[i-1] * dp4[i-1])%mod
    return (6 * dp4[n-2] * dp4[n-2])%mod

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    n = int(input().decode().strip())
    m = int(input().decode().strip())
    fixed_nodes = []
    for i in range(m):
        node,color = [x for x in input().decode().strip().split(" ")]
        fixed_nodes.append((node,color))
    resa = solve(n)
        # check(res)
    print(resa)

