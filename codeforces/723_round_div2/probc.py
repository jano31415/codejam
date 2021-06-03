from heapq import heapify, heappop, heappush
def solve(N, potions):
    # print(potions)
    cur_sum = 0
    tot = 0
    potions_taken = []
    heapify(potions_taken)
    for i,x in enumerate(potions):
        if cur_sum + x >= 0:
            heappush(potions_taken, x)
            tot += 1
            cur_sum += x
        else:
            heappush(potions_taken, x)
            minpot = heappop(potions_taken)
            # potions_taken.remove(minpot)
            # print(minpot)
            if minpot != x:
                cur_sum += x - minpot
    return tot

if __name__ == "__main__":
    # T = int(input())
    # for t in range(1, T + 1):
    N = input()
    potions = [int(x) for x in input().split(" ")]
    res = solve(N, potions)
    print("{res}".format(res=res), flush=True)

# import time
# import random
# a=time.time()
# potions = [random.randint(-10,20) for x in range(200000)]
# res = solve(len(potions), potions)
# print(len(potions))
# print(res)
# b=time.time()
# print(b-a)