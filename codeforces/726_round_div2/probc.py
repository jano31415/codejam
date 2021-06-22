def solve(N, mountains):
    mountains.sort()
    min_diff = 10**10
    min_index = 0
    for i,x in enumerate(mountains):
        if i == 0:
            continue
        if abs(mountains[i] - mountains[i-1]) < min_diff:
            min_diff = abs(mountains[i] - mountains[i-1])
            min_index = i
    res = [mountains[min_index-1]] + mountains[min_index+1:] + mountains[:min_index-1]+ [mountains[min_index]]
    res = [str(x) for x in res ]
    return " ".join(res)
import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        N = int(input().decode().strip())
        mountains = [int(x) for x in input().decode().strip().split(" ")]
        res = solve(N, mountains)
        print(res)