
def solve(N, numbers):
    set_numbers = set(numbers)
    if len(set_numbers) == N:
        return 0
    dyn = {d:0 for d in set_numbers}
    tot = 0
    for i,x in enumerate(numbers):
        tmp = dyn[x]
        tot += tmp * (N-i)
        dyn[x] = tmp + (i+1)
    return tot


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        numbers = [int(x) for x in input().split(" ")]
        res = solve(N, numbers)
        print(str(res), flush=True)

# import time
# import random
# a=time.time()
# N=10**5
# for i in range(20):
#     numbers=[random.randint(0,1000) for x in range(N)]
# solve(N,numbers)
# b=time.time()
# print(b-a)