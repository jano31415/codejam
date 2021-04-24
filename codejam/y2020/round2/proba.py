import math
def get_2sum(i,x):
    return i*x + x(x-1)

def solve_1sum(L, R):
    return math.ceil(-0.5 + math.sqrt(0.25 + 2*(L-R)))

def solve_2sum(remaining, i):
    sol = int(-(i-1)/2 + math.sqrt((i-1)**2/4 + remaining))
    return sol, remaining - (i*sol + sol*(sol-1))

def solve(L, R):
    swap = False
    if L < R:
        tmp = L
        L = R
        R = tmp
        swap = True
    i = solve_1sum(L, R)
    # print(f"L things {i}")
    remaining = L - (i*(i+1)//2)
    if remaining < 0:
        remaining += i
        i = i-1
    # print(remaining)
    if remaining == R and not swap:
        l_poss, reml = solve_2sum(remaining, i + 1)
        # print(f" possible remaining L {l_poss} {reml}")
        r_poss, remr = solve_2sum(R, i + 2)
        # print(f"possible R {r_poss} {remr}")
    else:
        l_poss, reml = solve_2sum(remaining, i+2)
        # print(f" possible remaining L {l_poss}")
        r_poss, remr = solve_2sum(R, i+1)
        # print(f"possible R {r_poss}")
        # print(i + l_poss + r_poss)
    toti = i + l_poss + r_poss
    if remr < 0:
        remr += toti
        toti -= 1
    if reml < 0:
        reml += toti
        toti -= 1
    if swap:
        return str(toti), str(remr), str(reml)
    return str(toti), str(reml), str(remr)

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        L, R = [int(x) for x in input().split(" ")]
        res = solve(L, R)
        print("Case #{t}: {res}".format(t=t, res=" ".join(res)), flush=True)



def solve_stupid(L,R):
    i=1
    while True:
        if L >= R:
            if L >= i:
                L = L - i
                i += 1
            else:
                break
        else:
            if R >= i:
                R = R - i
                i += 1
            else:
                break
    return str(i-1), str(L), str(R)

from random import randint
import time
a=time.time()
N=10**8
for _ in range(100):
    L = randint(1, N)
    R = randint(1, N)
    # print(f" L {L} R {R}")
    res1=solve(L, R)
    # print(res1)
b=time.time()
for _ in range(100):
    L = randint(1, N)
    R = randint(1, N)
    res2=solve_stupid(L, R)
    # print(res2)
    # assert res1 == res2
c=time.time()
print(b-a)
print(c-b)

for _ in range(1000):
    L = randint(1, N)
    R = randint(1, N)
    # print(f" L {L} R {R}")
    res1=solve(L, R)

    res2=solve_stupid(L, R)
    print(res2)
    print(res1)
    assert res1 == res2, res1