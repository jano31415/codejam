# import math
# def query(a,b):
#     print(f"? {a} {b}", flush=True)
#     answer = int(input())
#     # if answer == -1:
#     #     raise ValueError("some wrong query, probably query limit")
#     return answer

def solve(n, names):
    if n == 1:
        return names[0]
    if n == 2:
        # answer = query(names[0], names[1])
        print(f"? {names[0]} {names[1]}", flush=True)
        answer = int(input())
        if answer == 1:
            return names[0]
        else:
            return names[1]
    winners = names#[0]*(n//4)
    for i in range(n//4):
        cur = 4*i
        print(f"? {names[cur+1]} {names[cur+2]}", flush=True)
        answer = int(input())
        # answer = query(names[cur+1], names[cur+2])
        # a,b= cur,cur
        if answer == 0:
            a,b = cur, cur+3
        elif answer == 1:
            a,b = cur+1, cur+3
        elif answer == 2:
            a,b = cur, cur+2
        print(f"? {names[a]} {names[b]}", flush=True)
        answer = int(input())
        # answer = query(names[a], names[b])
        if answer == 1:
            winners[i] = names[a]
        else:
            winners[i] = names[b]
    # print(winners)
    return solve(n//4, winners)
from sys import stdin, stdout

def print(msg, flush=None):
    stdout.write(msg + '\n')
    stdout.flush()
import os
import io
if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    input = stdin.readline
    T = int(input())
    for t in range(T):
        n = int(input())
        winner=solve(2**n, list(range(1, 2**n + 1)))
        print(f"! {winner}", flush=True)

# import time
# a =time.time()
# for i in range(1000):
#     x = int(stdin.readline())
#     stdout.write("a")#str(x) + '\n')
#     stdout.flush()
# b=time.time()
# print(str(b-a))

# import time
# import os
# import io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# a =time.time()
# for i in range(1000):
#     x = int(input())
#     print(x, flush=True)
# b=time.time()
# print(b-a)

# import time
# a =time.time()
# for i in range(1000):
#     x = int(input())
#     print(x, flush=True)
# b=time.time()
# print(b-a)

