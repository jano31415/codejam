def solve(ram_a, ram_b,n,k):
    ram = list(zip(ram_a,ram_b))
    ram.sort()
    tot=k
    for a,b in ram:
        if tot >=a:
            tot+=b
        else:
            return tot
    return tot



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]

        ram_a = [int(x) for x in input().decode().strip().split()]
        ram_b = [int(x) for x in input().decode().strip().split()]
        res=solve(ram_a, ram_b,n,k)
        print(res, flush=True)
