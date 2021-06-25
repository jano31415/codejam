# does not work, try dp of solution
def solve(n, amounts):
    amounts = amounts[::-1]
    sol = []
    max_val = -1
    for i, rest in enumerate(amounts):
        if i <= max_val:
            continue
        if i >= len(amounts)-1:
            poss, res = find_last(rest)
            sol.append(res)
            if poss:
                break
            else:
                return "No", None

        works_left = get_works(amounts, i, rest, True)
        works_right = get_works(amounts, i, rest, False)
        if works_right[0] == works_left[0]:
            max_val = min(works_right[1], works_left[1])
            first=0
            second=1
            if works_right[1] > works_left[1]:
                first=1
                second=0
        else:
            max_val = max(works_right[0], works_left[0])
            first=0
            second=1
            if works_right[0] < works_left[0]:
                first=1
                second=0
        for j in range(i, max_val):
            sol.append(first)
        sol.append(second)
    amounts = amounts[::-1]
    sol = sol[:len(amounts)][::-1]
    possible = check_sol(amounts,sol)
    if possible:
        return "Yes", sol
    return "No", sol

def find_last(rest):
    k, a, b, c, d = rest
    if k>= a and k<=b:
        if c<=0 and 0<=d:
            return True, 0
    if c <= k and k <= d:
        if a<=0 and 0<=b:
            return True, 1

    return False, 0

def check_sol(amounts, sol):
    cur_left = 0
    cur_right = 0
    for i in range(len(amounts)):
        k, a, b, c, d = amounts[i]
        this_sol = sol[i]
        if this_sol == 0:
            cur_left=k
        else:
            cur_right=k
        if (cur_left < a) or (cur_left > b):
            return False
        if (cur_right < c) or (cur_right > d):
            return False
    return True


def get_works(amounts, i, rest, left):
    k, a, b, c, d = rest
    works = []
    for j in range(i, len(amounts)):
        kj, aj, bj, cj, dj = amounts[j]
        if len(works) == 2:
            break
        if left:
            a = max(a,aj)
            b = min(b,bj)
            if kj >= a and kj <= b:
                works.append(j)
        else:
            c = max(c,cj)
            d = min(d,dj)
            if kj >= c and kj <= d:
                works.append(j)
    if len(works) < 2:
        j = len(amounts)
        if left:
            if 0 >= a and 0 <= b:
                works.append(j)
        else:
            if 0 >= c and 0 <= d:
                works.append(j)
    if len(works) == 1:
        works.append(len(amounts)+1)
    if len(works) == 0:
        works = [len(amounts)+1, len(amounts)+2]
    return works

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n,m = [int(x) for x in input().decode().strip().split(" ")]
    amounts = []
    for i in range(n):
        k = int(input().decode().strip())
        a,b = [int(x) for x in input().decode().strip().split(" ")]
        c,d = [int(x) for x in input().decode().strip().split(" ")]

        amounts.append((k,a,b,c,d))
    res1,res2 = solve(n,amounts)
    print(res1)
    if res1 == "Yes":
        res2 = [str(x) for x in res2]
        print(" ".join(res2))