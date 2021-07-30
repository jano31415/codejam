def solve(s,t):
    # print(s)
    # print(t)
    for i,letter in enumerate(s):
        pointer = i
        if letter == t[0]:
            # if letter == t:
            #     return "YES"
            for j in range(min(len(s)-i, len(t))):
                right_moves = s[pointer+1:pointer+j+1]
                # print(right_moves)
                left_start = max(0, pointer+j-(len(t)-j-1))
                left_moves = s[left_start:pointer+j][::-1]
                # print(left_moves)
                # print(s[pointer]+right_moves + left_moves)
                if t == s[pointer]+right_moves + left_moves:
                    return "YES"
    return "NO"


import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        s=input().decode().strip()
        t=input().decode().strip()
        res=solve(s,t)
        print(res)