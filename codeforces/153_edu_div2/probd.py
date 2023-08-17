import math
import random


def solve(s):
    n=len(s)
    n0=s.count("0")
    n1=n-n0
    tot = n0*n1
    count10=0
    n0left = n0
    for x in s:
        if x == "0":
            n0left -= 1
        else: # "1"
            count10+=n0left
    if 2*count10 == tot:
        return 0
    unbalance = tot//2 - count10
    print(count10)
    if unbalance > 0:
        return solve(s[::-1])
    unbalance = abs(unbalance)
    res=0
    n0left = n0
    n1left = n1
    left = n
    for x in s:
        if x == "0":
            n0left -= 1
        else: # "1"
            # for i in range(n):
            #     left -=1
            #     if s[left] == "0":
            #         break
            #     else:
            #         n1left -= 1
            res+=1
            unbalance-=n0left#+n1left
            if unbalance <=0:
                return res

    return res

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    s = input().decode().strip()
    res=solve(s)
    print(res)
