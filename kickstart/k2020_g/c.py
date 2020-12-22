def solve(nr_wheels, max_val, wheels):
    minsum = max_val * nr_wheels
    for w in wheels:
        tmp = sum([min(abs(w-w_start),  max_val - abs(w_start - w)) for w_start in wheels])
        if tmp < minsum:
            minsum = tmp
    return minsum


def main():
    T = int(input())
    for t in range(1, T+1):
        nr_wheels, max_val = [int(x) for x in input().split(" ")]
        wheels = [int(x) for x in input().split(" ")]

        res = solve(nr_wheels, max_val, wheels)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
main()
############################### after challenge end ###

def solve_sort(nr_wheels, max_val, wheels):
    wheels.sort()
    print(wheels)
    cumsum = []
    tmp = 0
    for w in wheels:
        tmp += w
        cumsum.append(tmp)
    vals = []
    for i,w in enumerate(wheels):
        small = find_small_break(i, wheels, max_val)
        big = find_big_break(i, wheels, max_val)
        tot = 0
        if small == 0:
            tot += (i + 1) * w - cumsum[i]
        else:
            tot += cumsum[small-1] + small *(max_val-w)
            tot += (i-small) * w - (cumsum[i-1] - cumsum[small-1])
        print("left" + str(tot))
        if big == len(wheels)-1:
            tot += (cumsum[big]- cumsum[i]) - (big - i) * w
        else:
            tot += (len(wheels)-1- big) * w + max_val* (len(wheels)-1- big) -(cumsum[-1]- cumsum[big])
            tot += (cumsum[big]- cumsum[i]) - (big - i) * w
        print("right" +str(tot))
        print(small, big)
        vals.append(tot)

    return min(vals)

def find_small_break(i, wheels, max_val):
    if i == 0:
        return 0
    left = 0
    right = i
    while left != right:
        test_point = (left+right)//2
        if check_break_smaller(test_point, i, wheels, max_val):
            right = test_point
        else:
            if left == right - 1:
                left = right
            else:
                left = test_point

    return right


def check_break_smaller(test_point, i, wheels, max_val):
    return wheels[i] - wheels[test_point] >= max_val - wheels[test_point] + wheels[i]


def find_big_break(i, wheels, max_val):
    if i == len(wheels)-1:
        return len(wheels)-1
    left = i
    right = len(wheels)-1
    while left != right:
        test_point = (left + right) // 2
        if check_break_bigger(test_point, i, wheels, max_val):
            right = test_point
        else:
            if left == right - 1:
                left = right
            else:
                left = test_point

    return right


def check_break_bigger(test_point, i, wheels, max_val):
    return wheels[test_point] - wheels[i] >= max_val - wheels[test_point] + wheels[i]

import random
import time
def is_fast():
    n=100
    wheels = [random.randint(1,n) for x in range(5)]
    wheels = [2, 77, 86, 92 ,94]
    a=time.time()
    res1 = solve_sort(100, n, wheels)
    print(res1)
    b=time.time()
    print(b-a)
    res2 = solve(100, n, wheels)
    print(res2)
    #print(time.time()-b)
#test_fast()