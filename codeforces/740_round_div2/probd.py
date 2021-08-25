import math
def solve(n,m):
    dp = [1] * (n + 1) #div by x
    dp[1]=1
    dp[2] = 2
    dp_sum = dp[2]+dp[1]
    # count=0
    for j in range(1, n+1):
        #subtract
        if j >= 3:
            dp[j] = (dp[j] + dp_sum) % m
        # divison
        k=2
        # count = 0
        sqrt = math.sqrt(j)
        while k < j:
            if k > sqrt:
                a = (j//k)
                x = j % k
                how_many = 1 + x//a
            else:
                how_many=1
            dp[j] = (dp[j//k] * how_many + dp[j]) % m
            k += how_many
            # count+=1
            # print(k,j)
        dp[j] = (dp[j] - 1)%m
        dp_sum = (dp_sum + dp[j])%m
    # print(count)
    return dp[n]



import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    n,m = [int(x) for x in input().decode().strip().split(" ")]
    res = solve(n,m)
    # check(res)
    print(res)
b=time.time()
print(b-a)