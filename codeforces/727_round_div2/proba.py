def solve(n,x,t):
    if t < x:
        return 0
    cur_par = min(n-1, t//x)
    tot = (n-1 - cur_par) * cur_par
    tot += ((cur_par+1) * cur_par)//2
    return tot
import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,x,t = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,x,t)
        print(res)