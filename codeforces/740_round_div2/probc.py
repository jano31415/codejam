def solve(caves):
    for j,cave in enumerate(caves):
        caves[j] = [cave[i]-i for i in range(len(cave))]

    difficulty = [(max(a), len(a)) for a in caves]
    min_level = 0
    difficulty.sort(key=lambda x: x[0])
    cur = min_level
    for diff, size in difficulty:
        if diff >= cur:
            skill_needed = (diff-cur)+1
            cur += skill_needed
            min_level += skill_needed
        cur += size
    return min_level

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        caves = []
        for i in range(n):
            armors = [int(x) for x in input().decode().strip().split(" ")]
            armors.pop(0)
            caves.append(armors)
        res = solve(caves)
        # check(res)
        print(res)
