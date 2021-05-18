# problem a/ had the idea quite fast but did some mistake
# took 33mins.
COUNT = 0
def submit(s):
    log(f"Query: {s}")
    print(s, flush=True)

def get_input():
    a = int(input())
    log(f"Answer: {a}")
    return a

def log(s):
    pass
    # comment out logging to score at codejam
    # print(s, file=f)
import math
def solve(N, cost):
    # log start values
    log(f"T {T} N {N}")
    #submit with submit function
    for i in range(0,99):
        submit(f"M {i+1} {100}")
        cost+= math.ceil(10**8/(100-(i+1)+1))
        log(cost/10**8)
        # read answer from judge with get_input
        mid = int(get_input())
        if mid != i+1:
            submit(f"S {i+1} {mid}")
            success = int(get_input())
    submit("D")
    success = int(get_input())

with open("interactive.txt", "w+") as f:
    cost = 0
    T, N = [int(x) for x in input().split(" ")]
    for t in range(T):
        solve(N, cost)