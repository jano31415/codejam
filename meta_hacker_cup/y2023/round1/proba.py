def solve(n, elves):
    elves.sort()
    if n == 5:
        dist1 = (elves[-1] + elves[-2]) / 2 - (elves[0] + elves[2]) / 2
        dist2 = (elves[-1] + elves[-3]) / 2 - (elves[0] + elves[1]) / 2
        dist = max(dist1, dist2)
    else:
        dist = (elves[-1]+elves[-2])/2 - (elves[0]+elves[1])/2
    return dist

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    with open("out_a.txt", "w") as f:
        f.write("")
    T = int(input().decode().strip())
    for t in range(1,T+1):
        n = int(input().decode().strip())
        elves = [int(x) for x in input().decode().strip().split(" ")]
        res1=solve(n, elves)
        print(res1)
        with open("out_a.txt", "a") as f:
            f.write(f"Case #{t}: {res1}\n")
