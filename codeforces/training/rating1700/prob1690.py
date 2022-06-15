# so permutations can be split into cycles.
# least common denominator of the cycle lengths  is a solution
# but depending on the string there is an earlier one.

def solve(n,s, p):
    if n ==1:
        return 1
    cycles = [0]*n
    cycle_count = 1
    cycle_group = {}
    for i in range(n):
        if cycles[i] == 0:
            cycles[i] = cycle_count
            cycle_group[cycle_count] = [i]
            j = p[i]-1
            for _ in range(n):
                if j == i:
                    break
                cycles[j]=cycle_count
                cycle_group[cycle_count].append(j)
                j = p[j]-1
            cycle_count+=1
    lcd_list = [1]*(cycle_count-1)
    for c in range(1, cycle_count):
        group = cycle_group[c]
        group_same = [0]*len(group)
        for i,g in enumerate(group):
            last = g
            for j in range(len(group)//2+1):
                if s[p[g]-1] == s[p[last]-1]:
                    group_same[j] += 1
                last = p[last]-1
        min_group = len(group)
        for i in range(1, len(group)):
            if group_same[i] == len(group):
                min_group = i
                break
        lcd_list[c-1] = min_group
    sol = lcd_list[0]
    for i in range(1, len(lcd_list)):
        sol = lcm(sol, lcd_list[i])
    return sol


import math
def lcm(a, b):
    return a*b // math.gcd(a, b)

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()
        p = [int(x) for x in input().decode().strip().split()]
        res=solve(n, s, p)
        print(res)
# import time
# t1=time.time()
# a=list(range(2,201)) + [1]
# s="a"*200
# n=200
# solve(n,s,a)
# print((time.time()-t1)*5000)
