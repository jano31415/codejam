

import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        s = input().decode().strip()
        print(eval(s))
# import time
# a=time.time()
# n=10000
# solve(n=n, dep=[[]]+[set([i+2]) for i in range(n-1)]+[set()])
# b=time.time()
# print(b-a)