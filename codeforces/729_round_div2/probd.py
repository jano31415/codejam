from heapq import heapify, heappush, heappop
def solve(n, operations):
    res = 0
    mod = 998244353
    for j,start_op in enumerate(operations):
        if start_op[0] == "-":
            continue
        _,nr = start_op.split(" ")
        nr = int(nr)
        dp=[{} for _ in range(n+1)]
        dp[0][0]=1
        start_op_in = False
        for i,op in enumerate(operations):
            if i == j:
                for spot in dp[i]:
                    dp[i + 1][spot] = (dp[i + 1].get(spot,0) + dp[i][spot]) %mod
                start_op_in = True
                continue
            if op[0] == "+":
                _, nr_tmp = op.split(" ")
                nr_tmp = int(nr_tmp)
                if nr_tmp > nr or (nr_tmp == nr and i < j):

                    for spot in dp[i]:
                        dp[i+1][spot] = (dp[i+1].get(spot,0)+ 2*dp[i][spot]) % mod
                elif nr_tmp < nr or (nr_tmp == nr and i > j):
                    for spot in dp[i]:
                        if spot + 1 > (n-i):
                            dp[i + 1][spot-1] = (dp[i + 1].get(spot-1, 0) + dp[i][spot]) % mod
                            dp[i + 1][spot-1] = (dp[i + 1].get(spot-1, 0) + dp[i][spot]) % mod

                        else:
                            dp[i+1][spot+1] = (dp[i+1].get(spot+1,0) + dp[i][spot]) %mod
                            dp[i + 1][spot] = (dp[i + 1].get(spot,0)+ dp[i][spot]) % mod
                # equal
            else:
                for spot in dp[i]:
                    if spot != 0:
                        dp[i + 1][spot - 1] = (dp[i + 1].get(spot-1,0)+ dp[i][spot]) %mod
                    dp[i + 1][spot] = (dp[i + 1].get(spot,0)+  dp[i][spot]) %mod
                if not start_op_in:
                    dp[i+1][0] = (dp[i+1].get(0,0) + dp[i][0])%mod
        for spot in dp[-1]:
            res = (res + dp[-1].get(spot,0)*nr) %mod
    return res

def solve2(n, operations):
    T = []
    heapify(T)
    for op in operations:
        if op[0] == "+":
            a,b = op.split(" ")
            heappush(T,int(b))
        else:
            if len(T) > 0:
                dropthis = heappop(T)
    return sum(T)

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    n = int(input().decode().strip())
    operations =[]
    for i in range(n):
        op =input().decode().strip()
        operations.append(op)
    res = solve(n, operations)
    print(res)