import math
def solve(n,tokens):
    has_odd = any([x%2 == 1 for x in tokens])
    if has_odd:
        return sum([x % 2 == 0 for x in tokens])
    min2 = []
    for x in tokens:
        tot = 0
        while x%2 == 0:
            x = x//2
            tot+=1
        min2.append(tot)
    # print(min2)
    return (n-1) + min(min2)


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        tokens = [int(x) for x in input().decode().strip().split()]

        res=solve(n,tokens)
        print(res)

