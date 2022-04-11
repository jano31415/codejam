import numpy as np


def solve(n):
    pow2 = [2**i for i in range(30)]
    a = pow2 + list(range(130, 200))
    # with open("log.txt", "w") as f:
    #     print(len(a), file=f)
    a_str = [str(x) for x in a]
    print(" ".join(a_str), flush=True)
    b = [int(x) for x in input().split(" ")]
    # with open("log.txt", "w") as f:
    #     print(b, file=f)
    sumall = (sum(a) + sum(b))//2
    sola = []
    suma = 0
    solb = []
    sumb = 0
    notpow2 = list(range(130, 200)) + b
    for bi in notpow2:
        if suma <= sumb:
            sola.append(bi)
            suma += bi
        else:
            solb.append(bi)
            sumb += bi
    left = sumall - suma
    leftb = bin(left)[::-1]
    for ind, isin in enumerate(leftb[:-2]):
        if isin == "1":
            sola.append(pow2[ind])
    assert sum(sola) == sumall
    print(" ".join([str(x) for x in sola]), flush=True)



T = int(input())
for t in range(1, T+1):
    n = int(input())
    solve(n)
