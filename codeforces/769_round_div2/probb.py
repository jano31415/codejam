
import math
def solve(n):
    power2 = 1
    while 2*power2 < n:
        power2 = 2*power2
    l = list(range(1, power2))+[0,power2] + list(range(power2+1,n))
    # for i in range(8):
    #    l.append(power2 + l[pointer])
    #    pointer+=dir
    #    if pointer == len(l) or pointer == -1:
    #        dir = dir*-1
    #        power2 = 2*power2
    #        pointer+=dir
    # count_price(l)

    l = " ".join([str(x) for x in l])
    return l

def count_price(l):
    tot=0
    for i,x in enumerate(l):
        if i == len(l)-1:
            continue

        cur = l[i]^l[i+1]
        if cur > tot:
            tot = cur
    print(tot)
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res1 = solve(n)
        print(res1)
        # print("\n")

# print(count_price([int(x) for x in "4 6 3 2 0 8 9 1 7 5".split()]))