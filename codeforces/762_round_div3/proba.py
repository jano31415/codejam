def solve(s):
    if len(s) %2 == 1:
        return "NO"
    if s[:len(s)//2] == s[len(s)//2:]:
        return "YES"
    else:
        return "NO"






import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        s = input().decode().strip()

        res=solve(s)
        print(res, flush=True)
