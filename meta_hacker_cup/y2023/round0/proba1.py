def solve(s,d,k):
    bread = 2*s + 2*d
    patty = s + 2*d
    if (bread >= k+1) and (patty >= k):
        return "YES"
    return "NO"

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_a1.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        s,d,k = [int(x) for x in input().decode().strip().split(" ")]
        res1=solve(s,d,k)
        print(res1)
        with open("out_a1.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")
