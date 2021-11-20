import random
from collections import deque
def solve(n,s):
    right=deque(s)
    left =deque([])
    change=True
    while change:
        change=False
        while len(right) > 1:
            a = right.popleft()
            b = right[0]

            if (a == "9") or (a == "8"):
                left.append(a)
            elif int(b) == (int(a)+1) % 10:
                replace = str((int(a) + 2) % 10)
                right.popleft() # remove b as well
                right.appendleft(replace)
                if len(left) > 0:
                    tmp = left.pop()
                    right.appendleft(tmp)
            else:
                left.append(a)
        change=False
        if len(right) == 1:
            left.append(right.popleft())
        right = left
        left = deque([])
        while len(right) > 1:
            a = right.popleft()
            b = right[0]
            replace = str((int(a) +2)%10)
            if (int(a) < 8):
                left.append(a)
            elif int(b) == (int(a)+1) % 10:
                right.popleft() # remove b as well
                right.appendleft(replace)
                if len(left) > 0:
                    tmp = left.pop()
                    right.appendleft(tmp)
                change = True
            else:
                left.append(a)
        if len(right) == 1:
            left.append(right.popleft())
        right = left
        left = deque([])
    # right = left
    # left = deque([])
    return "".join(right)

def solve_old(n,s):
    right=deque(s)
    left =deque([])
    change=True
    while change:
        change=False
        for k in range(10):
            kstr = str(k)
            kstr2 = str((k+1) %10)
            replace = str((k+2)%10)
            for i in range(len(right)):
                if len(right) <= 1:
                    break
                a = right.popleft()
                b = right[0]
                if a == kstr and b == kstr2:
                    left.append(replace)
                    right.popleft() # remove b as well
                    change = True
                else:
                    left.append(a)
            if len(right) == 1:
                left.append(right.popleft())
            right = left
            left = deque([])
    return "".join(right)


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        s = input()

        res = solve(n, s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        # print(solve_old(n,s)

import random
from time import time
for i in range(1000):
    n=10
    s="".join([str(random.randint(0,9)) for i in range(n)])

    # l = list(range(n))
    # del l[len(l)//2]
    a=time()
    # for i in range(n-2):
    #     l.pop(0)
    res1=solve(len(s),s)
    res2 = solve_old(len(s), s)
    if res1 != res2:
        print(s)
    b=time()

n=500000
s="".join([str(random.randint(0,9)) for i in range(n)])
s ="0"+"13579"*1000
# l = list(range(n))
# del l[len(l)//2]
a=time()
# for i in range(n-2):
#     l.pop(0)
res1=solve(len(s),s)
res2 = solve_old(len(s), s)
if res1 != res2:
    print(s)
b=time()
print(b-a)
#
# print(b-a)
#
# l = deque(list(range(n)))
# del l[len(l)//2]
# a=time()
# for i in range(n-2):
#     l.popleft()
# b=time()
# print(b-a)