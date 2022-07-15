import math
def solve(n,a,b):
    ablock=to_block(a)
    bblock=to_block(b)
    # print(ablock)
    # print(bblock)

    if len(ablock) != len(bblock):
        return -1
    if a[0] != b[0]:
        return -1
    if a[-1] != b[-1]:
        return -1
    count=0
    for i in range(len(ablock)-1):
        if ablock[i] > bblock[i]:
            ablock[i+1] += ablock[i]-bblock[i]
            count += ablock[i]-bblock[i]
        elif ablock[i] < bblock[i]:
            bblock[i + 1] += bblock[i] - ablock[i]
            count += bblock[i] - ablock[i]
    return count
def to_block(a):
    last = a[0]
    count=0
    block=[]
    for ai in a:
        if ai==last:
            count+=1
        else:
            block.append(count)
            count=1
        last = ai
    block.append(count)
    return block

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a = input().decode().strip()
        b = input().decode().strip()
        res=solve(n,a,b)
        print(res)

