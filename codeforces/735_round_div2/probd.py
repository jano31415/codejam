import math
def solve(n):
    n = int(n)
    if n == 1:
        return "a"
    if n == 2:
        return "ab"
    if n == 3:
        return "abc"
    if n % 2 == 0:
        return ("a" * (n//2)) + "b" + ("a" * (n//2 - 1))
    else:
        return ("a" * (n//2)) + "bc" + ("a" * (n//2 - 1))

def check(s):
    print("checking " + s)
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            cur = s[i:j]
            c=0
            for a in range(len(s)):
                if s[a:a+(j-i)] == cur:
                    c+=1
            if c%2 == 0:
                print("even found")
                print(s[i:j])
                print(c)
                return
    print("none found")


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res = solve(n)
        # check(res)
        print(res)

