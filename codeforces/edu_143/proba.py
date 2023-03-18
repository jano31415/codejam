def solve(a,b,s1,s2):
    s = s1 + s2[::-1]
    tot=0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            tot+=1
    if tot>1:
        return "NO"
    return "YES"


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        a,b = [int(x) for x in input().decode().strip().split()]
        s1=input().decode().strip()
        s2=input().decode().strip()

        res = solve(a,b,s1,s2)
        print(res)