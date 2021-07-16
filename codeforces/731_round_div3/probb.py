def solve(s):
    alph = "abcdefghijklmnopqrstuvwxyz"
    if len(s) > 26:
        return False
    if len(s) == 0:
        return True
    if "a" not in s:
        return False

    right=s.index("a")
    left=right
    for i,a in enumerate(alph):
        if a== "a":
            continue
        if a not in s:
            if len(s) == i:
                return True
            else:
                return False
        if left > 0:
            if a == s[left-1]:
                left-=1
                continue
        if right < len(s)-1:
            if a == s[right+1]:
                right+=1
                continue
        return False
    return True

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        s=input().decode().strip()
        res = solve(s)
        if res:
            print("YES")
        else:
            print("NO")