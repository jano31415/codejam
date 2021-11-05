def solve(s):
    alph = "abcdefghijklmnopqrstuvwxyz"
    rev_map = {alph[i]:i for i in range(26)}
    min_s = "z"
    min_val = 27
    min_index = 0
    for i,x in enumerate(s):
        if rev_map[x] < min_val:
            min_val = rev_map[x]
            min_index = i
            min_s = x
    b = s[:min_index] + s[min_index+1:]
    return min_s, b



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        s = input().decode().strip()

        a,b = solve(s)
        # check(res)
        print(f"{a} {b}")
