def solve(a,b,c):
    if c < min(a,b):
        return 0
    if b >= 2*a:
        return c//a
    if b <= a:
        doubles = c//b
        if doubles < 1:
            return 0
        return 2*(c//b) - 1
    c = c-a
    singles = 1
    if c%b >= a:
        singles+=1
    return 2*(c//b) + singles


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_a2.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        a,b,c = [int(x) for x in input().decode().strip().split(" ")]
        res1=solve(a,b,c)
        print(res1)
        with open("out_a2.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")
