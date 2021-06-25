def solve(n, amounts):
    amounts.sort(key=lambda x:x[1])
    tot = sum([x[0] for x in amounts])
    cur = min(amounts[0][1], tot)
    waste = cur
    for a,b in amounts:
        if cur >= tot:
            return tot + waste
        if cur >= b:
            cur += a
        else:
            waste += min(tot,b) - cur
            cur = b+a
    return tot+waste


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n = int(input().decode().strip())
    amounts = []
    for i in range(n):
        a,b = [int(x) for x in input().decode().strip().split(" ")]
        amounts .append((a,b))
    res = solve(n,amounts)
    print(res)