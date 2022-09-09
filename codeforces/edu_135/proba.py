def solve(n,colors):
    max_i = 0
    max_x = colors[0]
    for i,x in enumerate(colors):
        if x > max_x:
            max_i = i
            max_x = x
    return max_i+1
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        colors = [int(x) for x in input().decode().strip().split()]
        res=solve(n, colors)
        print(res)

