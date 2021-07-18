def solve(n,a_score,b_score):
    ignore = n//4
    keep = n - ignore
    a_score.sort(reverse=True)
    b_score.sort(reverse=True)
    target = sum(b_score[:keep])
    current = sum(a_score[:keep])
    rounds_needed = 0
    keep_a = keep-1
    for j in range(1, 2*n+10):
        if current >= target:
            break
        rounds_needed = j
        if (n+j) % 4 != 0:
            current+=100
            if keep < n:
                target+=b_score[keep]
            keep+=1
        else:
            if keep_a >= 0:
                current= current+100 - a_score[keep_a]
                keep_a-=1

    return rounds_needed
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a_score=[int(x) for x in input().decode().strip().split(" ")]
        b_score=[int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,a_score,b_score)
        print(res)