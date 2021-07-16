def solve(n, seq):
    y_seq = ["0"]*n
    last = "{0:b}".format(seq[0])[::-1]
    for j,x in enumerate(seq[1:]):
        x_bin = "{0:b}".format(x)[::-1]
        max_len = max(len(x_bin), len(last))
        x_bin = x_bin.ljust(max_len, "0")
        last = last.ljust(max_len, "0")
        # print(x_bin)
        # print(last)
        y = 0
        exp = 0
        for i,dig in enumerate(x_bin):
            if (last[i] == "1") and (dig == "0"):
                y+=2**exp
            exp+=1
        y_seq[j+1] = str(y)
        if y != 0:
            last = "{0:b}".format(x+y)[::-1]
        else:
            last = x_bin
    return " ".join(y_seq)

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        seq=[int(x) for x in input().decode().strip().split(" ")]
        res = solve(n,seq)
        print(res)

# import random
# n=2*10**5
# l = []
# x=0
# for i in range(n):
#     y=random.randint(0,100)
#     l.append(x+y)
#     x= x+y
# import time
# a =time.time()
# solve(n,l)
# b =time.time()
# print(b-a)
