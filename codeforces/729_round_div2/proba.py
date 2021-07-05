def solve(n, numbers):
    even =[x for x in numbers if x%2 ==0]
    odd = [x for x in numbers if x%2 ==1]
    if len(even) == len(odd):
        print("Yes")
    else:
        print("No")

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        numbers = [int(x) for x in input().decode().strip().split(" ")]
        solve(n, numbers)
