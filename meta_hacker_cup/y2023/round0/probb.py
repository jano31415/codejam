def solve(r,c,a,b):
    if r > c:
        return "YES"
    return "NO"


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_b.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        r,c,a,b = [int(x) for x in input().decode().strip().split(" ")]
        res1=solve(r,c,a,b)
        print(res1)
        with open("out_b.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")
