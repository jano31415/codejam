def solve(s):
    if "1" not in s:
        return 1
    if "0" not in s:
        return 0
    zeros = 0
    cur_zero=False
    for x in s:
        if x == "0":
            if not cur_zero:
                zeros += 1
                cur_zero = True
        if x == "1":
            cur_zero = False
        if zeros == 2:
            break
    return min(zeros,2)
import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        s =input().decode().strip()
        a = solve(s)
        print(a)

