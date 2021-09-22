def solve(a,b,c,m):
    tmp = [a,b,c]
    tmp.sort()
    c,b,a = tmp
    min_val = (a-1)-b-c
    max_val = max(0,(a-1)) + max(0,(b-1)) + max(0,(c-1))
    if (m >= min_val) and (m <= max_val):
        return "YES"
    return "NO"

import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        a,b,c,m =[int(x) for x in input().decode().strip().split(" ")]
        a = solve(a,b,c,m)
        print(a)