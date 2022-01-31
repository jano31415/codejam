import math
def solve(n, s):
    if "00" in s:
        return "NO"
    if "11" in s:
        return "NO"
    if "101" in s:
        return "NO"
    if "010" in s:
        return "NO"
    return "YES"
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()
        res1 = solve(n, s)
        print(res1)
        # print("\n")