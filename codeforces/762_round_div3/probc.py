import math
def solve(a,s):
    a=a[::-1]
    s=s[::-1]
    cur_i =0
    b=[]
    for i in range(len(a)):
        ai = int(a[i])
        if cur_i >= len(s):
            return -1
        si = int(s[cur_i])
        if ai <= si:
            b.append(str(si-ai))
        else:
            b.append(str(10+si-ai))
            cur_i +=1
            if cur_i >= len(s):
                return -1
            if s[cur_i] != "1":
                return -1
        cur_i += 1

    if cur_i != len(s):
        for _ in range(len(s)):
            if cur_i >= len(s):
                break
            b.append(s[cur_i])
            cur_i+=1

    return "".join(b[::-1]).lstrip("0")


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        a,s = [x for x in input().decode().strip().split(" ")]

        res=solve(a,s)
        print(res, flush=True)
